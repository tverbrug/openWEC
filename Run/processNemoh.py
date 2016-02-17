# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 16:04:58 2015

This script uses the prony method to approximate the Impulse Response
Function of a floating WEC by a sum of complex exponential functions.

@author: tverbrug
"""

import numpy as np

def calcAlphaBeta(nSel,rho,dof):

#---------------------------------------------------------------------------
# INPUT
#---------------------------------------------------------------------------
    
    # Open IRF file
    #rho = 1025.0
    #nSel = 10
    #dof = 'all'
    pathFile = './Run/Nemoh/IRF.tec'
    with open(pathFile,'r') as f:
        irfRaw = f.readlines()
    if sum(dof) < 2:
        strPat = 'DoF    1'
        irfInd = 2
    elif dof[2] == 1:
        strPat = 'DoF    {:d}'.format(sum(dof[0::2]))
        irfInd = sum(dof[0::2])*2
    else:
        strPat = 'DoF    1'
        irfInd = 2
    for iL in range(0,len(irfRaw)):
        irfInfo = irfRaw[iL]
        test = irfInfo.find(strPat)
        if test!=-1:
            indStart = iL
            irfInfo = irfInfo.split()
            irfNrlong = irfInfo[3]
            indComma = irfNrlong.index(',')
            irfNr = int(irfNrlong[0:indComma])
    # Arrange data in IRF file
    time = [0]*irfNr
    IRF = [0]*irfNr
    for iL in range(indStart+1,irfNr+indStart+1):
        irfLine = irfRaw[iL].split()
        time[iL-indStart-1] = float(irfLine[0])
        IRF[iL-indStart-1] = float(irfLine[irfInd])
    aInf = float(irfLine[irfInd-1])    
    
#---------------------------------------------------------------------------
# CALCULATION
#---------------------------------------------------------------------------
    
    IRF = np.array(IRF)
    dt = time[2]-time[1]
    m = 200
    n = len(IRF)-m-1
    
# STEP1: make polynome R with values s_k
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
    
    A = np.zeros((n+1,m))
    for i in range(0,n+1):
        A[i,:] = IRF[i:i+m]
    C = -IRF[m:n+m+2]
    R,res,ran,sing = np.linalg.lstsq(A,C)
    del res,ran,sing
    R = np.append(R,1)
    R = np.flipud(R)
    
# STEP2: find roots of polynomial R
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
    
    Q = np.roots(R)
    
# STEP3: Calculate Beta
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
    
    beta = np.log(Q)/dt
    del A,C,R
    
# STEP3: Calculate Alpha
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
    
    Q2 = np.zeros((n+1,m));
    Q2 = np.array(Q2,dtype=complex)
    for i in range(0,n+1):
        Q2[i,:] = np.transpose(Q)**i
    F = IRF[0:n+1]
    C,res,ran,sing = np.linalg.lstsq(Q2,F)
    del res,ran,sing
    alpha = C*np.exp(-beta*time[1])
    del F,Q,Q2,C
    
# STEP5: only consider beta-values with a negative real part, so function goes
# to zero
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
    
    mask = np.real(beta)<0
    alpha = alpha[mask] 
    beta = beta[mask] 
    m = len(alpha)
    
#---------------------------------------------------------------------------
# SELECTION of alpha en beta components
#---------------------------------------------------------------------------
    
# STEP1: Sorting of values
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
    absVal = -np.abs(np.divide(alpha,beta))
    indSort = np.flipud(np.argsort(absVal))
    alpha = np.flipud(alpha[indSort])
    beta = np.flipud(beta[indSort])

# STEP2: Complex conjugate checking
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
    
    test1 = np.abs(np.imag(alpha[nSel-1]))
    test2 = np.abs(np.imag(alpha[nSel]))
    if np.abs(test1-test2)<0.001:
        nSel = nSel + 1
    alphaSel = alpha[0:nSel]
    betaSel = beta[0:nSel]
    
#---------------------------------------------------------------------------
# CALCULATE Error
#---------------------------------------------------------------------------
    
# STEP1: Reconstruction of the IRF
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
    
    mat1 = np.matrix(np.ones((len(IRF), 1)))
    mat2 = np.matrix(alphaSel)
    mat3 = np.transpose(np.matrix(time))*np.matrix(betaSel)
    fMatrix = np.multiply(mat1*mat2,np.exp(mat3))
    fRecons = np.sum(fMatrix,axis=1)
    
# STEP2: Calculation of the error
#-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
    
    diff1 = fRecons[1:len(IRF)/2]
    diff2 = np.transpose(np.matrix(IRF[1:len(IRF)/2]))
    diff3 = np.matrix(IRF)
    relDiffE = np.abs(diff1-diff2)/np.max(np.abs(diff3))
    error2E = np.abs(np.sum(relDiffE)/((len(IRF))/2))
    
#---------------------------------------------------------------------------
# PLOT Result
#---------------------------------------------------------------------------
    
    #plt.plot(time,IRF)
    #plt.plot(time,np.real(fRecons))
    
    return (alphaSel,betaSel,error2E,aInf)
    
def calcM(rho=1025.0,dof=[0,0,1,0,0,0]):
    pathFile = './Run/Nemoh/KH.dat'
    dof = np.array(dof)
    with open(pathFile,'r') as f:
        khRaw = f.readlines()
    KH = np.zeros((6,6))
    for iL in range(len(khRaw)):
        KH[iL,:] = np.array([float(a) for a in khRaw[iL].split()])
    if sum(dof)>1:
        c = KH
    else:
        dof = list(dof)
        c = np.dot(KH,dof)[dof.index(1)]
    
    M = np.diag([1.,1.,1.,1.,1.,1.])
    pathFile = './Run/Nemoh/Hydrostatics.dat'
    with open(pathFile,'r') as f:
        mRaw = f.readlines()
    mass = rho*float(mRaw[3].split()[2])
    M[0:3,0:3] *= mass
    zG = float(mRaw[2].split()[-1])
    M[0,4] = mass*zG
    M[1,3] = -mass*zG
    M[4,0] = mass*zG
    M[3,1] = -mass*zG
    
    I = np.zeros((3,3))    
    pathFile = './Run/Nemoh/Inertia_hull.dat'
    with open(pathFile,'r') as f:
        mRaw = f.readlines()
    for iL in range(len(mRaw)):
        I[iL,:] = np.array([float(a) for a in mRaw[iL].split()])
    M[3::,3::] *= I
    if sum(dof)>1:
        None
    else:
        M = np.dot(M,dof)[dof.index(1)]
    return (M,c)
    
def writeOutputNemoh(M,Mainf,c,alpha,beta):
    pathFile = './Run/Nemoh/outNemoh.dat'
    fid = open(pathFile,'w')
    inString = '{0:e}'
    fid.write('Mass:\t'+inString.format(M)+'\n')
    fid.write('Mainf:\t'+inString.format(Mainf)+'\n')
    fid.write('c:\t'+inString.format(c)+'\n')
    fid.write('=========================================================\n')
    fid.write('ALPHA\n')
    fid.write('=========================================================\n')
    for iA in range(0,len(alpha)):
        fid.write(str(np.real(alpha[iA])) + '\t' + str(np.imag(alpha[iA])) + '\n')
    fid.write('=========================================================\n')
    fid.write('BETA\n')
    fid.write('=========================================================\n')
    for iB in range(0,len(beta)):
        fid.write(str(np.real(beta[iB])) + '\t' + str(np.imag(beta[iB])) + '\n')
    fid.close()
    
def getPeriod():
    pathFile = './Run/Nemoh/Fe.dat'
    with open(pathFile,'r') as f:
        irfRaw = f.readlines()
        omega = [0]*(len(irfRaw)-3)
        for iL in range(3,len(irfRaw)):
            irfInfo = irfRaw[iL]
            irfInfo = irfInfo.split()
            omega[iL-3] = float(irfInfo[0])
    omega = np.array(omega)
    period = 2*np.pi/omega
    return period
            
def getAB(dof,nbody=1,sel=10):
    # Selected DOF
    if sum(dof)<2:
        selDof = dof.index(1)
        # Open Radiation Coefficients    
        pathFile = './Run/Nemoh/RadiationCoefficients.tec'
        with open(pathFile,'r') as f:
            irfRaw = f.readlines()
        strPat = 'body    1 in DoF   ' + str(sum(dof[0:selDof+1]))
        irfInd = 1 + sum(dof[0:selDof])*2
        for iL in range(0,len(irfRaw)):
            irfInfo = irfRaw[iL]
            test = irfInfo.find(strPat)
            if test!=-1:
                indStart = iL
                irfInfo = irfInfo.split()
                irfNrlong = irfInfo[8]
                indComma = irfNrlong.index(',')
                irfNr = int(irfNrlong[0:indComma])
        # Arrange data in RadiationCoefficients file
        A = np.zeros(irfNr)
        B = np.zeros(irfNr)
        omega = np.zeros(irfNr)
        for iL in range(indStart+1,irfNr+indStart+1):
            irfLine = irfRaw[iL].split()
            A[iL-indStart-1] = float(irfLine[irfInd])
            B[iL-indStart-1] = float(irfLine[irfInd+1])
            omega[iL-indStart-1] = float(irfLine[0])

        
    else:
        omega = 2*np.pi/getPeriod()
        nrF = len(omega)
        A = np.zeros((6,6,nrF))
        B = np.zeros((6,6,nrF))
        
        # Open Radiation Coefficients    
        pathFile = './Run/Nemoh/RadiationCoefficients.tec'
        with open(pathFile,'r') as f:
            irfRaw = f.readlines()
        irfRaw = irfRaw[2+sum(dof)::]
        
        indList = []
        dof2 = [a for a in dof]
        for iD in range(sum(dof)):
            indList.append(dof2.index(1))
            dof2[dof2.index(1)] = 0
        
        for iA in range(sum(dof)):
            i1 = indList[iA]
            for iL in range(0,len(omega)):
                dummy = [float(a) for a in irfRaw[iL].split()[1::]]
                for iD in 2*np.array(range(sum(dof))):
                    i2 = indList[iD/2]
                    A[i1,i2,iL] = dummy[iD]
                    B[i1,i2,iL] = dummy[iD+1]
            irfRaw = irfRaw[nrF+1::]

        if sel > 5:
            None
        else:
            A = A[sel,sel,:]
            B = B[sel,sel,:]

    return(A,B,omega)
        
def getFe(dof,sel=10,nbody=1):
    # Selected DOF
    if sum(dof)<2:
        selDof = dof.index(1)
        # Open Radiation Coefficients    
        pathFile = './Run/Nemoh/ExcitationForce.tec'
        with open(pathFile,'r') as f:
            irfRaw = f.readlines()
        strPat = 'I='
        irfInd = 1 + sum(dof[0:selDof])*2
        for iL in range(0,len(irfRaw)):
            irfInfo = irfRaw[iL]
            test = irfInfo.find(strPat)
            if test!=-1:
                indStart = iL
                irfInfo = irfInfo.split()
                irfNrlong = irfInfo[8]
                indComma = irfNrlong.index(',')
                irfNr = int(irfNrlong[0:indComma])
        # Arrange data in RadiationCoefficients file
        FeMod = np.zeros(irfNr)
        FeAng = np.zeros(irfNr)
        for iL in range(indStart+1,irfNr+indStart+1):
            irfLine = irfRaw[iL].split()
            FeMod[iL-indStart-1] = float(irfLine[irfInd])
            FeAng[iL-indStart-1] = abs(float(irfLine[irfInd+1]))
    else:
        omega = 2*np.pi/getPeriod()
        nrF = len(omega)
        FeMod = np.zeros((6,nrF))
        FeAng = np.zeros((6,nrF))
        
        # Open Radiation Coefficients    
        pathFile = './Run/Nemoh/ExcitationForce.tec'
        with open(pathFile,'r') as f:
            irfRaw = f.readlines()
        irfRaw = irfRaw[2+sum(dof)::]
        
        indList = []
        dof2 = [a for a in dof]
        for iD in range(sum(dof)):
            indList.append(dof2.index(1))
            dof2[dof2.index(1)] = 0
        
        for iL in range(0,len(omega)):
            dummy = [float(a) for a in irfRaw[iL].split()[1::]]
            for iD in 2*np.array(range(sum(dof))):
                i2 = indList[iD/2]
                FeMod[i2,iL] = dummy[iD]
                FeAng[i2,iL] = dummy[iD+1]

        if sel > 5:
            None
        else:
            FeMod = FeMod[sel,:]
            FeAng = FeAng[sel,:]

    # Return values
    return(FeMod,FeAng)

def irregAB(Ma,Bhyd,omega,M,c,dof,specSS):
    # Calculate RAO
    FeMod,FeAng = getFe(dof)
    raoPitch = (FeMod[4,:])/np.abs(-omega**2.0*(M[4,4] + Ma[4,4,:])-1j*omega*Bhyd[4,4,:]+c[4,4])
    # Find Peak
    BhydS = Bhyd[:,:,np.argmax(raoPitch)]
    BhydS[2,2] = 0.0
    # Calculate mean added mass
    MaS = np.zeros(np.shape(BhydS))
    for iF in range(len(omega)):
        MaS += specSS[iF]*Ma[:,:,iF]
    MaS = MaS/(np.sum(specSS))
    
    return MaS, BhydS
    
def getMesh(nbody=1):
    if nbody == 1:
        # Open Radiation Coefficients    
        pathFile = './Calculation/mesh/axisym_info.dat'
        with open(pathFile,'r') as f:
            line = f.readlines()
            lineData = line[0].split()
            nP = int(lineData[0])
            nT = int(lineData[1])
        pathFile = './Calculation/mesh/axisym.dat'
        x = np.zeros((nP))
        y = np.zeros((nP))
        z = np.zeros((nP))
        trii = np.zeros((2*nT,3))
        iT = 0
        with open(pathFile,'r') as f:
            line = f.readlines()
        for iP in range(nP):
            data = line[iP+1].split()
            x[iP] = data[1]
            y[iP] = data[2]
            z[iP] = data[3]
        for iTr in range(nT):
            data = line[nP+2+iTr].split()
            trii[iT,:] = [int(data[0])-1,int(data[1])-1,int(data[2])-1]
            trii[iT+1,:] = [int(data[0])-1,int(data[2])-1,int(data[3])-1]
            iT += 2
    else:
        nP = np.zeros(nbody+1,dtype=int)
        nT = np.zeros(nbody+1,dtype=int)
        for iB in range(nbody):
            # Open Radiation Coefficients    
            pathFile = './Calculation/mesh/axisym{0:d}_info.dat'.format(iB+1)
            with open(pathFile,'r') as f:
                line = f.readlines()
                lineData = line[0].split()
                nP[iB+1] = int(lineData[0])
                nT[iB+1] = int(lineData[1])
                
        x = np.zeros(sum(nP))
        y = np.zeros(sum(nP))
        z = np.zeros(sum(nP))
        trii = np.zeros((2*sum(nT),3))
        
        for iB in range(nbody):
            pathFile = './Calculation/mesh/axisym{0:d}.dat'.format(iB+1)
            iT = 2*nT[iB]
            iL = 1
            with open(pathFile,'r') as f:
                line = f.readlines()
            for iP in range(nP[iB],nP[iB]+nP[iB+1]):
                data = line[iL].split()
                x[iP] = data[1]
                y[iP] = data[2]
                z[iP] = data[3]
                iL+=1
            iL = 2
            for iTr in range(nT[iB],nT[iB]+nT[iB+1]):
                data = line[nP[iB+1]+iL].split()
                trii[iT,:] = [int(data[0])-1+nP[iB],int(data[1])-1+nP[iB],int(data[2])-1+nP[iB]]
                trii[iT+1,:] = [int(data[0])-1+nP[iB],int(data[2])-1+nP[iB],int(data[3])-1+nP[iB]]
                iT += 2
                iL += 1
    # Return values
    return(x,y,z,trii)

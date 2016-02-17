# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 09:15:11 2015

This module is a collection of several functions
used to run the Nemoh software package in linux

@author: tverbrug
"""
import math
import os
import shutil as sh
import platform as pt


# Used Functions

def createMeshAxi(r,z,n,dtheta):
    nx = 0
    thetaR = range(0,dtheta)
    theta = [xx*math.pi/(dtheta-1) for xx in thetaR]
    # write mesh file
    if not os.path.exists('./Calculation/mesh'):
        os.makedirs('./Calculation/mesh')    
    fid = open('./Calculation/mesh/axisym','w')
    values = str(n*dtheta) + '\n'
    fid.write(values)
    values = str((n-1)*(dtheta-1)) + '\n'
    fid.write(values)     
    # calculate coordinates of mesh nodes
    for iT in range(0,dtheta):
        for iN in range(0,n):
            x = r[iN]*math.cos(theta[iT])
            y = r[iN]*math.sin(theta[iT])
            zz = z[iN]
            values = str(x) + '\t' + str(y) + '\t' + str(zz) + '\n'
            fid.write(values)
            nx = nx+1
    # calculate connections
    nf = 0
    for iN in range(1,n):
        for iT in range(1,dtheta):
            NN1 = iN+n*(iT-1)
            NN2 = iN+1+n*(iT-1)
            NN3 = iN+1+n*iT
            NN4 = iN+n*iT
            values = str(NN1) + '\t' + str(NN2) + '\t' + str(NN3) + '\t' + str(NN4) + '\n'   
            fid.write(values)            
            nf = nf + 1        
    
    # close mesh file
    fid.close()             

def createMeshFull(n,X):
    nx = 0
    # write mesh file
    if not os.path.exists('./Calculation/mesh'):
        os.makedirs('./Calculation/mesh')    
    fid = open('./Calculation/mesh/axisym','w')
    values = str(n*4) + '\n'
    fid.write(values)
    values = str(n) + '\n'
    fid.write(values)     
    # calculate coordinates of mesh nodes and connections
    for pan in X:
        for point in pan:
            x = point[0]
            y = point[1]
            z = point[2]
            values = '{0:E} {1:E} {2:E} \n'.format(x,y,z)
            fid.write(values)
            nx += 1
    for iC in range(n):
        values = '{0:g} {1:g} {2:g} {3:g} \n'.format(4*iC+1,4*iC+2,4*iC+3,4*iC+4)
        fid.write(values)
    # close mesh file
    fid.close()             

def createMeshOpt(zG,nPanels,nsym,rho=1025.0,g=9.81,nbody=1,xG=0.0):
    if nbody==1:
        fid = open('./Calculation/Mesh.cal','w')
        fid.write('axisym\n')
        fid.write('{:d}\n'.format(nsym))
        fid.write('0. 0.\n')
        value = '0. 0. {0:f} \n'.format(zG)
        fid.write(value)
        fid.write(str(nPanels) + '\n')
        fid.write('2\n0.\n1.\n')
        fid.write('{0:f}\n'.format(rho))
        fid.write('{0:f}\n'.format(9.81))
        fid.close()
        os.chdir('Calculation')
        os.system('Mesh.exe')
        os.chdir('../')
    else:
        for iB in range(nbody):
            fid = open('./Calculation/Mesh.cal','w')
            fid.write('axisym{:d}\n'.format(iB+1))
            fid.write('{:d}\n'.format(nsym))
            fid.write('0. 0.\n')
            value = '{0:f} 0. {1:f} \n'.format(xG[iB],zG)
            fid.write(value)
            fid.write(str(nPanels) + '\n')
            fid.write('2\n0.\n1.\n')
            fid.write('{0:f}\n'.format(rho))
            fid.write('{0:f}\n'.format(9.81))
            fid.close()
            os.chdir('Calculation')
            os.system('Mesh.exe')
            os.chdir('../')

def writeCalFile(rhoW,depW,omega,zG,dof,aO={},nbody=1,xG=[0.0]):
    # Read info on the mesh
    nrNode = [0]*nbody
    nrPanel = [0]*nbody
    for iB in range(nbody):
        if nbody == 1:
            f1 = open('./Calculation/mesh/axisym_info.dat','r')
        else:
            f1 = open('./Calculation/mesh/axisym{:d}_info.dat'.format(iB+1),'r')
        lineInfo = f1.readline()
        lineInfo = lineInfo.split()
        nrNode[iB] = int(lineInfo[0])
        nrPanel[iB] = int(lineInfo[1])
        f1.close()
    # Read advanced options if there are any
    dirCheck = aO['dirCheck']
    irfCheck = aO['irfCheck']
    kochCheck = aO['kochCheck']
    fsCheck = aO['fsCheck']

    # Create the Nemoh calibration file
    fid = open('./Calculation/Nemoh.cal','w')
    fid.write('--- Environment ---\n')
    fid.write(str(rhoW) + '				! RHO 			! KG/M**3 	! Fluid specific volume\n')
    fid.write('9.81				! G			! M/S**2	! Gravity\n')
    fid.write(str(depW) + '				! DEPTH			! M		! Water depth\n')
    fid.write('0.	0.			! XEFF YEFF		! M		! Wave measurement point\n')
    fid.write('--- Description of floating bodies ---\n')
    fid.write('{:d}				! Number of bodies\n'.format(nbody))
    for iB in range(nbody):      
        fid.write('--- Body {:d} ---\n'.format(iB+1))
        if nbody == 1:
            fid.write('axisym.dat			! Name of mesh file\n')
        else:
            fid.write('axisym{:d}.dat			! Name of mesh file\n'.format(iB+1))
        fid.write(str(nrNode[iB]) + '\t' + str(nrPanel[iB]) + '			! Number of points and number of panels\n')
        fid.write('{:d}				! Number of degrees of freedom\n'.format(sum(dof)))
        for iDof in range(len(dof)):
            if (iDof == 0 and dof[iDof] == 1):
                fid.write('1 1. 0.	0. 0. 0. 0.		! Surge\n')
            elif (iDof == 1 and dof[iDof] == 1):
                fid.write('1 0. 1.	0. 0. 0. 0.		! Sway\n')
            elif (iDof == 2 and dof[iDof] == 1):
                fid.write('1 0. 0. 1. 0. 0. 0.		! Heave\n')
            elif (iDof == 3 and dof[iDof] == 1):
                fid.write('2 1. 0. 0. {0:f} 0. {1:f}		! Roll about CdG\n'.format(xG[iB],zG))
            elif (iDof == 4 and dof[iDof] == 1):
                fid.write('2 0. 1. 0. {0:f} 0. {1:f}		! Pitch about CdG\n'.format(xG[iB],zG))
            elif (iDof == 5 and dof[iDof] == 1):
                fid.write('2 0. 0. 1. {0:f} 0. {1:f}		! Yaw about CdG\n'.format(xG[iB],zG))
        fid.write('{:d}				! Number of resulting generalised forces\n'.format(sum(dof)))
        for iDof in range(len(dof)):
            if (iDof == 0 and dof[iDof] == 1):
                fid.write('1 1. 0.	0. 0. 0. 0.		! Force in X direction\n')
            elif (iDof == 1 and dof[iDof] == 1):
                fid.write('1 0. 1.	0. 0. 0. 0.		! Force in Y direction\n')
            elif (iDof == 2 and dof[iDof] == 1):
                fid.write('1 0. 0. 1. 0. 0. 0.		! Force in Z direction\n')
            elif (iDof == 3 and dof[iDof] == 1):
                fid.write('2 1. 0. 0. {0:f} 0. {1:f}		! Roll Moment about CdG\n'.format(xG[iB],zG))
            elif (iDof == 4 and dof[iDof] == 1):
                fid.write('2 0. 1. 0. {0:f} 0. {1:f}		! Pitch Moment about CdG\n'.format(xG[iB],zG))
            elif (iDof == 5 and dof[iDof] == 1):
                fid.write('2 0. 0. 1. {0:f} 0. {1:f}		! Yaw Moment about CdG\n'.format(xG[iB],zG))
        fid.write('0				! Number of lines of additional information\n')
    
    fid.write('--- Load cases to be solved ---\n')
    fid.write(str(omega[0]) + '\t' + str(omega[1]) + '\t' + str(omega[2]) + '		! Number of wave frequencies, Min, and Max (rad/s)\n')
    if dirCheck:
        fid.write(str(aO['dirStep']) + '\t' + str(aO['dirStart']) + '\t' + str(aO['dirStop']) + '		! Number of wave directions, Min and Max (degrees)\n')
    else:
        fid.write('1	0.	0.		! Number of wave directions, Min and Max (degrees)\n')
    fid.write('--- Post processing ---\n')
    if irfCheck:
        fid.write('1' + '\t' + str(aO['irfStep']) + '\t' + str(aO['irfDur']) + '\t\t! IRF 				! IRF calculation (0 for no calculation), time step and duration\n')
    else:
        fid.write('0' + '\t0.01\t20.\t\t! IRF 				! IRF calculation (0 for no calculation), time step and duration\n')
    fid.write('0				! Show pressure\n')
    if kochCheck:
        fid.write(str(aO['kochStep']) + '\t' + str(aO['kochStart']) + '\t' + str(aO['kochStop']) + '		! Kochin function 		! Number of directions of calculation (0 for no calculations), Min and Max (degrees)\n')
    else:
        fid.write('0	0.	180.		! Kochin function 		! Number of directions of calculation (0 for no calculations), Min and Max (degrees)\n')
    if fsCheck:
        fid.write(str(aO['fsDeltaX']) + '\t' + str(aO['fsDeltaY']) + '\t' + str(aO['fsLengthX']) + '\t' + str(aO['fsLengthY']) + '	! Free surface elevation 	! Number of points in x direction (0 for no calcutions) and y direction and dimensions of domain in x and y direction	\n')
    else:
        fid.write('0	2	1000.	2.	! Free surface elevation 	! Number of points in x direction (0 for no calcutions) and y direction and dimensions of domain in x and y direction	\n')
    
    fid.close()

def runNemoh(nbody=1):
    os.chdir('./Calculation')
    if nbody == 1:
        sh.copyfile('./mesh/axisym.dat','axisym.dat')
    else:
        for iB in range(nbody):
            sh.copyfile('./mesh/axisym{:d}.dat'.format(iB+1),'axisym{:d}.dat'.format(iB+1))
    if pt.system()=='Linux':
        os.system('../Nemoh/preProc')
        os.system('../Nemoh/solver')
        os.system('../Nemoh/postProc')
    else:
        os.system('preProcessor.exe')
        os.system('Solver.exe')
        os.system('postProcessor.exe')
    os.chdir('../')


def postNemoh(dof):
    # Open IRF file
    with open('./Calculation/results/IRF.tec','r') as f:
        irfRaw = f.readlines()
        if dof=='heave':
            strPat = 'DoF    1'
            irfInd = 2
        else:
            strPat = 'DoF    3'
            irfInd = 6
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
    timeIRF = [0]*irfNr
    dataIRF = [0]*irfNr
    for iL in range(indStart+1,irfNr+indStart+1):
        irfLine = irfRaw[iL].split()
        timeIRF[iL-indStart-1] = float(irfLine[0])
        dataIRF[iL-indStart-1] = float(irfLine[irfInd])

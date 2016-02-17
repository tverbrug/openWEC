# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 17:01:56 2015

@author: tverbrug
"""

import scipy.integrate  as sci
import numpy as np


def simBody1DOF(time,Fex,Fdamp,dampType,M,Mainf,c,alpha,beta):
    
  
    # Initial Conditions
    y0 = [0.0, 0.0]
    arg_f = [M,Mainf,c,Fex[0],0.0]
    if dampType==0:
        arg_f[4] = Fdamp
    for iA in range(0,len(alpha)):
        y0.append(0.0)
        arg_f.append(alpha[iA])
    for iA in range(0,len(alpha)):
        arg_f.append(beta[iA])
       
    t0 = time[0]    
    
    # Define System
    def fC(t, y, args):
        rhs = [0]*int((len(args)-5)/2+2)       
        rhs[0] = y[1]
        rhs[1] = 0.0
        I = ''
        for iB in range(0,len(rhs)-2):
            I = I + '-y[' + str(2+iB) + ']'
            rhs[iB+2] = args[iB+(len(args)-5)/2+5]*y[iB+2]+args[iB+5]*y[1]
        rhs[1] = eval('(args[3]-args[4]-args[2]*y[0]' + I + ')/(args[0]+args[1])')
        return rhs

    def fL(t, y, args):
        rhs = [0]*int((len(args)-5)/2+2)       
        rhs[0] = y[1]
        rhs[1] = 0.0
        I = ''
        for iB in range(0,len(rhs)-2):
            I = I + '-y[' + str(2+iB) + ']'
            rhs[iB+2] = args[iB+(len(args)-5)/2+5]*y[iB+2]+args[iB+5]*y[1]
        rhs[1] = eval('(args[3]-args[4]*y[1]-args[2]*y[0]' + I + ')/(args[0]+args[1])')
        return rhs

    # Define Tuning
    def ptoForce(r,Fdamp,Fe,c):
        vel = r.y[1]
        pos = r.y[0]
        nI = len(r.y)-2
        I = 0.0
        for iI in range(0,nI):
            I = I + r.y[iI+2]
        Fwa = Fe-c*pos-I
        if vel<0.0:
            Fpto = 0.0
        elif vel>0.02:
            Fpto = Fdamp
        else:
            Fcom = np.array([Fdamp,Fwa])
            Fcom = np.array([Fcom.min(),0.0])            
            Fpto = Fcom.max()
        return Fpto
    
    # Set-up System
    if dampType == 0:
        r = sci.ode(fL).set_integrator('dopri5')
    else:
        r = sci.ode(fC).set_integrator('dopri5')
    r.set_initial_value(y0, t0).set_f_params(arg_f)
    
    t1 = time[-1]
    dt = time[1]-time[0]
    z = np.zeros(len(time))
    Fp = np.zeros(len(time))
    v = np.zeros(len(time))
    tim = np.zeros(len(time))
    iF = 0
    
    while r.successful() and r.t < t1:
        r.integrate(r.t+dt)
        z[iF] = r.y[0]
        v[iF] = r.y[1]
        tim[iF] = r.t
        arg_f[3] = Fex[iF]
        if dampType == 0:
            Fp[iF] = Fdamp*v[iF]
        else:
            dummy = ptoForce(r,Fdamp,Fex[iF],c)
            arg_f[4] = dummy
            Fp[iF] = dummy
        r.set_f_params(arg_f)
        iF = iF + 1
    
    return tim,z,v,Fp

def simBodyReg1DOF(time,Fex,Fdamp,dampType,M,c,Ma,Bhyd):
    
    # Ramp function for Fex
    ramp = 0.5*(1+np.tanh(2*np.pi/10.0*time-np.pi))
    Fex = Fex*ramp
    
    # Initial Conditions
    y0 = [0.0, 0.0]
    arg_f = [M,c,Ma,Bhyd,Fex[0],0.0]
    if dampType == 0:
        arg_f[5] = Fdamp

    t0 = time[0]    

    # Define System
    def fC(t, y, args):
        rhs = [0]*2       
        rhs[0] = y[1]
        rhs[1] = (args[4] - args[3]*y[1] - args[5] - args[1]*y[0])/(args[0] + args[2])
        return rhs
        
    def fL(t, y, args):
        rhs = [0]*2       
        rhs[0] = y[1]
        rhs[1] = (args[4] - args[3]*y[1] - args[5]*y[1] - args[1]*y[0])/(args[0] + args[2])
        return rhs

    # Define Tuning
    def ptoForce(r,Fdamp,Fe,c,Bhyd):
        vel = r.y[1]
        pos = r.y[0]
        Fwa = Fe-c*pos-Bhyd*vel
        if vel<0.0:
            Fpto = 0.0
        elif vel>0.02:
            Fpto = Fdamp
        else:
            Fcom = np.array([Fdamp,Fwa])
            Fcom = np.array([Fcom.min(),0.0])            
            Fpto = Fcom.max()
        return Fpto
    
    
    if dampType == 0:
        r = sci.ode(fL).set_integrator('dopri5')
    else:
        r = sci.ode(fC).set_integrator('dopri5')
    r.set_initial_value(y0, t0).set_f_params(arg_f)
    
    t1 = time[-1]
    dt = time[1]-time[0]
    z = np.array([0])
    v = np.array([0])
    Fp = np.array([0])
    tim = np.array([0])
    iF = 0
    
    while r.successful() and r.t < t1:
        r.integrate(r.t+dt)
        z = np.append(z,r.y[0])
        v = np.append(v,r.y[1])
        tim = np.append(time,r.t)
        y0 = r.y
        arg_f[4] = Fex[iF]
        if dampType == 1:
            dummy = ptoForce(r,Fdamp,Fex[iF],c,Bhyd)
            arg_f[5] = dummy
            Fp = np.append(Fp,dummy)
        else:
            Fp = np.append(Fp,Fdamp*r.y[1])
        r.set_f_params(arg_f)
        iF = iF + 1
    
    tim = np.delete(tim,-1)
    
    return tim,z,v,Fp

def simBodyReg(time,Fex,Fdamp,dampType,M,c,Ma,B):
    
    # Initial Conditions
    y0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    arg_f = [M[0,0],M[1,1],M[2,2],M[3,3],M[4,4],M[5,5],M[0,4],M[1,3],
             Ma[0,0],Ma[1,1],Ma[2,2],Ma[3,3],Ma[4,4],Ma[5,5],Ma[0,4],Ma[1,3],            
             B[0,0],B[1,1],B[2,2],B[3,3],B[4,4],B[5,5],B[0,4],B[1,3],
             c[2,2],c[3,3],c[4,4],Fex[0,0],Fex[1,0],Fex[2,0],Fex[3,0],
             Fex[4,0],Fex[5,0]]
       
    t0 = time[0]    
    
    def f(t, y, args):
        rhs = [0]*12       
        rhs[0] = y[6]
        rhs[1] = y[7]
        rhs[2] = y[8]
        rhs[3] = y[9]
        rhs[4] = y[10]
        rhs[5] = y[11]
        rhs[6] = (args[27]-(args[6]+args[14])*rhs[10]-args[16]*y[6]-args[22]*y[10])/(args[0] + args[8])
        rhs[7] = (args[28]-(args[7]+args[15])*rhs[9]-args[17]*y[7]-args[23]*y[9])/(args[1] + args[9])
        rhs[8] = (args[29]-args[18]*y[8]-args[24]*y[2])/(args[2] + args[10])
        rhs[9] = (args[30]-(args[7]+args[15])*rhs[7]-args[19]*y[9]-args[23]*y[7]-args[25]*y[3])/(args[3] + args[11])
        rhs[10] = (args[31]-(args[6]+args[14])*rhs[6]-args[20]*y[10]-args[22]*y[6]-args[26]*y[4])/(args[4] + args[12])
        rhs[11] = (args[32]-args[21]*y[11])/(args[5] + args[13])
        return rhs
        
    r = sci.ode(f).set_integrator('lsoda',nsteps = 50)
    r.set_initial_value(y0, t0).set_f_params(arg_f)
    
    t1 = time[-1]
    dt = time[1]-time[0]
    xx = np.zeros((6,len(time)))
    vv = np.zeros((6,len(time)))
    tim = np.array([0])
    iF = 0
    
    while r.successful() and r.t < t1:
        r.integrate(r.t+dt)
        xx[:,iF] = r.y[0:6]
        vv[:,iF] = r.y[6::]
        tim = np.append(time,r.t)
        y0 = r.y
        
        arg_f[27] = Fex[0,iF]
        arg_f[28] = Fex[1,iF]
        arg_f[29] = Fex[2,iF]
        arg_f[30] = Fex[3,iF]
        arg_f[31] = Fex[4,iF]
        arg_f[32] = Fex[5,iF]
        
        r.set_f_params(arg_f)
        iF = iF + 1
    
    tim = np.delete(tim,-1)
    
    return tim,xx,vv

def simBody(time,Fex,Fdamp,dampType,M,Ma,B,c,alpha,beta):
    
    # Initial Conditions
    y0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    arg_f = [M[0,0],M[1,1],M[2,2],M[3,3],M[4,4],M[5,5],M[0,4],M[1,3],
             Ma[0,0],Ma[1,1],Ma[2,2],Ma[3,3],Ma[4,4],Ma[5,5],Ma[0,4],Ma[1,3],            
             B[0,0],B[1,1],B[2,2],B[3,3],B[4,4],B[5,5],B[0,4],B[1,3],
             c[2,2],c[3,3],c[4,4],Fex[0,0],Fex[1,0],Fex[2,0],Fex[3,0],
             Fex[4,0],Fex[5,0]]
             
    for iA in range(0,len(alpha)):
        y0.append(0.0)
        arg_f.append(alpha[iA])
    for iA in range(0,len(alpha)):
        arg_f.append(beta[iA])
   
    t0 = time[0]    
    
    def f(t, y, args):
        rhs = [0]*int((len(args)-33)/2 + 12)       
        rhs[0] = y[6]
        rhs[1] = y[7]
        rhs[2] = y[8]
        rhs[3] = y[9]
        rhs[4] = y[10]
        rhs[5] = y[11]
        rhs[6] = (args[27]-(args[6]+args[14])*rhs[10]-args[16]*y[6]-args[22]*y[10])/(args[0] + args[8])
        rhs[7] = (args[28]-(args[7]+args[15])*rhs[9]-args[17]*y[7]-args[23]*y[9])/(args[1] + args[9])
        #rhs[8] = (args[29]-args[18]*y[8]-args[24]*y[2])/(args[2] + args[10])
        rhs[8] = 0.0
        I = ''
        for iB in range(0,len(rhs) - 12):
            I = I + ' - y[' + str(12+iB) + ']'
            rhs[iB+12] = args[iB+(len(args)-33)/2+33]*y[iB+2]+args[iB+33]*y[1]
        rhs[8] = eval('(args[29] - args[24]*y[2]' + I + ')/(args[2]+args[10])')
        rhs[9] = (args[30]-(args[7]+args[15])*rhs[7]-args[19]*y[9]-args[23]*y[7]-args[25]*y[3])/(args[3] + args[11])
        rhs[10] = (args[31]-(args[6]+args[14])*rhs[6]-args[20]*y[10]-args[22]*y[6]-args[26]*y[4])/(args[4] + args[12])
        rhs[11] = (args[32]-args[21]*y[11])/(args[5] + args[13])
        return rhs
        
    r = sci.ode(f).set_integrator('lsoda',nsteps = 50)
    r.set_initial_value(y0, t0).set_f_params(arg_f)
    
    t1 = time[-1]
    dt = time[1]-time[0]
    xx = np.zeros((6,len(time)))
    vv = np.zeros((6,len(time)))
    tim = np.array([0])
    iF = 0
    
    while r.successful() and r.t < t1:
        r.integrate(r.t+dt)
        xx[:,iF] = r.y[0:6]
        vv[:,iF] = r.y[6:12]
        tim = np.append(time,r.t)
        y0 = r.y
        
        arg_f[27] = Fex[0,iF]
        arg_f[28] = Fex[1,iF]
        arg_f[29] = Fex[2,iF]
        arg_f[30] = Fex[3,iF]
        arg_f[31] = Fex[4,iF]
        arg_f[32] = Fex[5,iF]
        
        r.set_f_params(arg_f)
        iF = iF + 1
    
    tim = np.delete(tim,-1)
    
    return tim,xx,vv

    
def saveResults(saveName,time,pos_z,vel_z,Fpto,li=[0]):
    check = len(np.shape(pos_z))
    dofName = ['Surge','Sway','Heave','Roll','Pitch','Yaw']
    if check > 1:
        f = open(saveName,'w')
        for iDof in li:
            f.write('Degree of Freedom: ' + dofName[iDof] + '\n')
            f.write('Time(s),Position(m),Velocity(m/s),Fdamp(N)\n')
            for iLine in range(len(time)):
                putLine = '{0:.2f},{1:.4f},{2:.4f},{3:.4f}\n'.format(
                    time[iLine],pos_z[iDof,iLine],vel_z[iDof,iLine],Fpto[iDof,iLine])
                f.write(putLine)
        f.close()    
    else:
        f = open(saveName,'w')
        f.write('Time(s),Position(m),Velocity(m/s),Fdamp(N)\n')
        for iLine in range(len(time)):
            putLine = '{0:.2f},{1:.4f},{2:.4f},{3:.4f}\n'.format(
                time[iLine],pos_z[iLine],vel_z[iLine],Fpto[iLine])
            f.write(putLine)
        f.close()    

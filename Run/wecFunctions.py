# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 13:12:58 2015

This is a collection of functions, used in the WEC simulation tool

@author: tverbrug
"""

import numpy as np

#---------------------------------------------------------------------------
# SPECTRAL VALUES
#---------------------------------------------------------------------------

def spectralValue(Hs,Tm,freqs):
    # Determine necessary parameters    
    fp = 1/(1.2958*Tm)
    gamma = 3.3
    alpha = 0.0624/(0.230 + 0.0336*gamma - (0.185/(1.9+gamma))) 
    freq_n = len(freqs)
    beta = np.zeros(freq_n)
    specSS = np.zeros(freq_n)
    # Calculate spectrum
    for iS in range(0,freq_n):
        if freqs[iS] < fp:
            sigma = 0.07
        else:
            sigma = 0.09
        beta[iS] = np.exp(-(freqs[iS]-fp)**2/(2*sigma**2*fp**2))
        specSS[iS] = alpha*Hs**2*fp**4*freqs[iS]**(-5)*gamma**beta[iS]*np.exp(-5/4.0*(fp/freqs[iS])**4)
    # Return values
    return specSS
    
def makeWavex(t,f,S,phase,Fa,Fp):
    # Make new frequencies and spectrum, with interpolated values
    nf = 140
    f_new = np.linspace(f[0],f[-1],nf)
    S = np.interp(f_new,f,S)
    check = len(np.shape(Fa))
    if check > 1:
        Famp = np.zeros((6,nf))
        Fpha = np.zeros((6,nf))
        for iD in range(6):
            Famp[iD,:] = np.interp(f_new,f,Fa[iD,:])
            Fpha[iD,:] = np.interp(f_new,f,Fp[iD,:])
        force = np.zeros((6,len(t),len(f_new)))
    else:
        Famp = np.interp(f_new,f,Fa)
        Fpha = np.interp(f_new,f,Fp)
        force = np.zeros((len(t),len(f_new)))    
    
    # Pre allocation
    deltaf = np.abs(f_new[0]-f_new[1])
    zta = np.sqrt(2*S*deltaf)
    wave = np.zeros((len(t),len(f_new))) 
    phase = list(reversed(phase)) 
    # Loop over all frequencies
    
    if check > 1:
        for iF in range(0,len(f_new)):
            wave[:,iF] = zta[iF]*np.cos(2*np.pi*f_new[iF]*t + phase[iF])
            for iD in range(6):
                force[iD,:,iF] = zta[iF]*Famp[iD,iF]*np.cos(2*np.pi*f_new[iF]*t + phase[iF] - Fpha[iD,iF])
        # Sum over all frequencies
        tot_wave = np.sum(wave,axis=1)
        tot_force = np.sum(force,axis=2)
    else:
        for iF in range(0,len(f_new)):
            wave[:,iF] = zta[iF]*np.cos(2*np.pi*f_new[iF]*t + phase[iF])
            force[:,iF] = zta[iF]*Famp[iF]*np.cos(2*np.pi*f_new[iF]*t + phase[iF] - Fpha[iF])
        # Sum over all frequencies
        tot_wave = np.sum(wave,axis=1)
        tot_force = np.sum(force,axis=1)
    
    return(tot_wave,tot_force)

def makeWavexReg(t,Hs,Tm,f,S,Famp,Fpha):
    # Make new frequencies and spectrum, with interpolated values
    f_new = 1.0/Tm
    S = np.interp(f_new,f,S)
    check = len(np.shape(Famp))
    if check > 1 :
        oI = np.interp(f_new,f,f)
        mask = [a > 0 for a in f - oI]
        iS,iE = (mask.index(True)-1,mask.index(True))
        Famp = Famp[:,iS] + (Famp[:,iE]-Famp[:,iS])*(oI-f[iS])/(f[iE]-f[iS])
        Fpha = Fpha[:,iS] + (Fpha[:,iE]-Fpha[:,iS])*(oI-f[iS])/(f[iE]-f[iS])
    else:
        Famp = np.interp(f_new,f,Famp)
        Fpha = np.interp(f_new,f,Fpha)
    # Loop over all frequencies
    wave = Hs/2.0*np.cos(2*np.pi*f_new*t)
    if check > 1 :
        force = np.zeros((6,len(t)))
        for iF in range(6):
            force[iF,:] = Hs/2.0*Famp[iF]*np.cos(2*np.pi*f_new*t - Fpha[iF])
    else:
        force = Hs/2.0*Famp*np.cos(2*np.pi*f_new*t - Fpha)
    return(wave,force)

    
def makePhase():
    nPhase = 50
    pathFile = './Run/phaseVectors.dat'    
    with open(pathFile,'r') as f:
        phaseRaw = f.readlines()
    
    phaseOK = phaseRaw[nPhase]
    phaseOK = phaseOK.split()
    phaseVector = [float(iP) for iP in phaseOK]    
    
    return phaseVector
    
def calcRAO(Fe,M,Ma,B,c,w):
    rao = np.absolute(Fe/(-w**2*(M+Ma) + 1j*w*(B) + c))
    return rao
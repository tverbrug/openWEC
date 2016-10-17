# -*- coding: utf-8 -*-
"""
Created on Fri Feb 06 16:19:53 2015

@author: tverbrug
"""

import processNemoh as pn
import wecFunctions as wf
import numpy as np
import os

wdir = os.path.join(os.path.expanduser("~"),'openWEC')


def makeWaveFex(Hs,Tm,time,dof,wavType,Sout=False,CS=False):

#-----------------------------------------------------------------------------
# CALCULATION
#-----------------------------------------------------------------------------
    
# Get the wave frequencies out of the Nemoh results
    period = pn.getPeriod()
    freqs = 1.0/period
    
# Calculate the spectral values
    if CS:
        try:
            specFile = os.path.join(wdir,'Other','spec.dat')
            data = np.loadtxt(specFile)
            f = data[:,0]
            s = data[:,1]
            specSS = np.interp(freqs,f,s)
        except:
            print("Warning! No custom spectrum defined, default spectrum selected!")
            specSS = wf.spectralValue(Hs,Tm,freqs)
    else:
        specSS = wf.spectralValue(Hs,Tm,freqs)
    
# Get hydrodynamic coefficients from Nemoh
    FeAmp,FePha = pn.getFe(dof)
    
# Construct phaseVector
    phaseVector = wf.makePhase()
    
# Calculate Wave Excitation Signal
    if wavType=='irregular':
        Wave,Fex = wf.makeWavex(time,freqs,specSS,phaseVector,FeAmp,FePha)
    else:
        Wave,Fex = wf.makeWavexReg(time,Hs,Tm,freqs,specSS,FeAmp,FePha)
    
    if Sout:
        return(time,Wave,Fex,specSS)
    else:
        return(time,Wave,Fex)

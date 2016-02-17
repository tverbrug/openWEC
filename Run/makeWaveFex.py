# -*- coding: utf-8 -*-
"""
Created on Fri Feb 06 16:19:53 2015

@author: tverbrug
"""

import processNemoh as pn
import wecFunctions as wf

def makeWaveFex(Hs,Tm,time,dof,wavType,Sout=False):

#-----------------------------------------------------------------------------
# CALCULATION
#-----------------------------------------------------------------------------
    
# Get the wave frequencies out of the Nemoh results
    period = pn.getPeriod()
    freqs = 1.0/period
    
# Calculate the spectral values
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

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:28:32 2016

@author: drsmith
"""

from warnings import warn

import matplotlib.pyplot as plt

from fdp.classes.utilities import isSignal, isContainer
from fdp.classes.fdp_globals import FdpWarning
from fdp.classes.fft import Fft
from . import utilities as UT

def fft(obj, *args, **kwargs):
    """
    Calculate FFT(s) for signal or container.
    Return Fft instance from classes/fft.py
    """
    
    if isSignal(obj):
        return Fft(obj, *args, **kwargs)
    elif isContainer(obj):
        signalnames = UT.get_signals_in_container(obj)
        ffts = []
        for sname in signalnames:
            signal = getattr(obj, sname)
            ffts.append(Fft(signal, *args, **kwargs))
        return ffts

def plotfft(signal, fmax=None, *args, **kwargs):
    """
    Plot spectrogram
    """
    if not isSignal(signal):
        warn("Method valid only at signal-level", FdpWarning)
        return
    sigfft = fft(signal, *args, **kwargs)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    pcm = ax.pcolormesh(sigfft.time, 
                        sigfft.freq, 
                        sigfft.logpsd.transpose(), 
                        cmap=plt.cm.YlGnBu)
    pcm.set_clim([sigfft.logpsd.max()-100, sigfft.logpsd.max()-20])
    #ax.set_ylim([0,200])
    cb = plt.colorbar(pcm, ax=ax)
    cb.set_label(r'$10\,\log_{10}(|FFT|^2)$ $(V^2/Hz)$')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Frequency (kHz)')
    if fmax:
        if sigfft.iscomplexsignal:
            ax.set_ylim([-fmax,fmax])
        else:
            ax.set_ylim([0,fmax])
    ax.set_title('{} | {} | {}'.format(
                 sigfft.shot, 
                 sigfft.parentname.upper(), 
                 sigfft.signalname.upper()))
    return sigfft

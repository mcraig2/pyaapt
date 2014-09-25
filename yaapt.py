""" This script implements YAAPT algorithm. More information can be found
    here: http://harvey.binghamton.edu/~hhu1/paper/Zahorian2008spectral.pdf """

import scipy
import numpy as np
from scipy.signal import butter
from scipy.signal import lfilter


# Runs the YAAPT algorithm to pull out fundamental frequencies for each time
def yaapt(data, sample_rate=44100):
    # Separate out the signal into the regular and the non-linearly
    # transformed signal, afterwards bandpass filtering both.
    # TODO - bandpass filter
    signal, signal_nonlinear = bandpass_filter(data), bandpass_filter(data ** 2)

    # Return the fundamental frequency
    #return freqs


#####################################################################################
if __name__ == '__main__':
    import os
    import sys
    import pylab as pl
    from scipy.io import wavfile

    # Read in a WAV file of a Saxophone playing A220
    this_folder = os.path.dirname(os.path.abspath(__file__))
    sample_rate, wav_data = wavfile.read(this_folder + '/sample_sax_A220.wav')

    # Pull out the fundamental frequency from the signal
    #freqs = yaapt(wav_data, sample_rate)
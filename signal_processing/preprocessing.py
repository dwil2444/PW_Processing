import numpy as np
from scipy import signal


class preprocessing():
    # Normalise pulse wave to occupy range of 0 to 1
    def normalise(waveform):
        range = np.ptp(waveform, axis=0)
        min = np.min(waveform)
        waveform = (waveform - min) / range
        return waveform


    def butter_lowpass(cutoff, fs, order=2):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
        return [b, a]


    def butter_lowpass_filter(waveform, cutoff, fs, order=4):
        b, a = preprocessing.butter_lowpass(cutoff, fs, order=order)
        y = signal.lfilter(b, a, waveform)
        # remove linear trend
        y = signal.detrend(y)
        return y



# PWs were preprocessed by 1) removing very high frequencies with a low-pass filter with 􏰋3-dB cutoff frequency of 16.75 Hz;
# 2) removing very low frequencies by subtracting any linear trend be- tween PW onset and end; and 3) aligning PWs to start
# at the beginning of the systolic upslope.
import numpy as np


class identify_fid_points():
    def identify_sys_peak(waveform):
        sys_peak = np.amax(waveform)
        peak_idx = np.argmax(waveform)
        return[sys_peak, peak_idx]

    def identify_dicr_notch(waveform, sys_peak_idx):
        sub_wave = int(0.6 * waveform.size)
        # waveform = waveform[sys_peak_idx: sub_wave]
        dic_notch_idx = 0
        dic_notch = waveform[dic_notch_idx]
        for i in range(0, waveform.size):
            if(i > sys_peak_idx and i < sub_wave):
                if (waveform[i+1] > waveform[i]):
                    dic_notch_idx = i
                    dic_notch = waveform[dic_notch_idx]
                    return [dic_notch, dic_notch_idx]
        dic_notch = waveform[dic_notch_idx]
        return [dic_notch, dic_notch_idx]
        # first_grad = np.gradient(waveform)
        # ms = np.argmax(first_grad)
        # second_grad = np.gradient(first_grad)
        # search_range = second_grad[ms+1: len(second_grad)]
        # dic_notch_idx = np.argmax(search_range)
        # dic_notch = waveform[dic_notch_idx]
        # return [dic_notch, dic_notch_idx]


    def identify_dias_peak(waveform, dic_notch_idx):
        sub_wave = int(0.6 * waveform.size)
        print(sub_wave)
        sub_waveform = waveform[dic_notch_idx + 1: sub_wave]
        print(dic_notch_idx)
        dias_peak_idx = np.argmax(sub_waveform, 0) + dic_notch_idx
        dias_peak = waveform[dias_peak_idx]
        print(dias_peak, dias_peak_idx)
        return [dias_peak, dias_peak_idx]

    def identify_sys_up(waveform):
        sys_peak, peak_idx = identify_fid_points.identify_sys_peak(waveform)
        sys_up = (sys_peak - waveform[0])/(peak_idx - 0)
        return sys_up


# reduce whatever deviation over threshold value


# preprocessing module - normalize/truncate signal input

# smoothing module - remove excessively high or low frequencies

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import signal_processing
import os
import statistics

files = os.listdir("csv_files")
num_files = len(files)
print(num_files)
sys_peak_values = []
dias_peak_values = []
dic_notch_values = []
sys_up_values = []

sys_peak_idx_values = []
dias_peak_idx_values = []
dic_notch_idx_values = []


for i in range(1, num_files - 2):
    wavefilename = "csv_files/myfile{0}.csv".format(i)
    wf_values = np.genfromtxt(wavefilename, delimiter=',')  # PPG_Carotid

    if (len(wf_values) > 400):
        wf_values = wf_values[0:400]

    wf_normal = signal_processing.preprocessing.normalise(wf_values)

    sos = signal.butter(3, 0.04, output='sos', analog=False)

    y = signal.sosfiltfilt(sos, wf_normal)

    # y = wf_normal

    # y = signal_processing.preprocessing.butter_lowpass_filter(wf_normal, 16.75, 500, 2)

    sys_peak, peak_idx = signal_processing.identify_fid_points.identify_sys_peak(y)
    dic_notch, dic_notch_idx = signal_processing.identify_fid_points.identify_dicr_notch(y, peak_idx)

    # dic_notch = 0.95
    # dic_notch_idx = 100
    dias_peak, dias_peak_idx = signal_processing.identify_fid_points.identify_dias_peak(y, dic_notch_idx)
    sys_upstroke = signal_processing.identify_fid_points.identify_sys_up(y)

    print(sys_upstroke)  # sys_upstroke ratio

    # z = signal.find_peaks(y)

    plt.annotate("Sys_Peak", (peak_idx, sys_peak))
    plt.annotate("Dic_Notch", (dic_notch_idx, dic_notch))
    plt.annotate("Dia_Peak", (dias_peak_idx, dias_peak))
    plt.plot(y)
    plt.show()
    if(peak_idx < dias_peak_idx and peak_idx < dic_notch_idx):
        sys_peak_values.append(sys_peak)
        dias_peak_values.append(dias_peak)
        dic_notch_values.append(dic_notch)
        sys_up_values.append(sys_upstroke)

        sys_peak_idx_values.append(peak_idx)
        dias_peak_idx_values.append(dias_peak_idx)
        dic_notch_idx_values.append(dic_notch_idx)

    # else:
    #     pass

sys_peak_values.sort()
dias_peak_values.sort()
dic_notch_values.sort()
sys_up_values.sort()

sys_peak_idx_values.sort()
dias_peak_idx_values.sort()
dic_notch_idx_values.sort()

med_sys_peak = statistics.median(sys_peak_values)
med_dias_peak = statistics.median(dias_peak_values)
med_dic_notch = statistics.median(dic_notch_values)
med_sys_up = statistics.median(sys_up_values)
med_sys_peak_idx = statistics.median(sys_peak_idx_values)
med_dias_peak_idx = statistics.median(dias_peak_idx_values)
med_dic_notch_idx = statistics.median(dic_notch_idx_values)

print('Systolic Peak Median: {0}'.format(med_sys_peak))
print('Diastolic Peak  Median: {0}'.format(med_dias_peak))
print('Dicrotic Notch Median: {0}'.format(med_dic_notch))
print('Systolic Upstroke Median: {0}'.format(med_sys_up))
print('Systolic Peak Index Median: {0}'.format(med_sys_peak_idx))
print('Diastolic Peak Index Median: {0}'.format(med_dias_peak_idx))
print('Dicrotic Notch Index Median: {0}'.format(med_dic_notch_idx))










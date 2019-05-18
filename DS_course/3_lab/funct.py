import os
import sys
import csv
import pandas as pd
import numpy as np
from random import sample

def filter_and_write_csv(txt_file):
    df=pd.read_csv(txt_file, index_col=False, header=0, sep=";", low_memory=False)
    df=df[df['Voltage'] != '?']
    df[['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2']]=df[['Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2']].astype(float)
    df.index=range(len(df))
    df.to_csv('Clean_data.txt', float_format='%.3f', index=0)

def frame():
    txt_file="Clean_data.txt"
    df=pd.read_csv(txt_file, index_col=False, header=0, low_memory=False)
    df1=df[df['Global_active_power'] > 5.000]
    df1.to_csv('Global_active_power_more_5.csv', float_format='%.3f', index=0)
    df2=df[df['Voltage'] > 235.000]
    df2.to_csv('Voltage_more_235.csv', float_format='%.3f', index=0)
    df3=df[df['Global_intensity'] >= 19.000]
    df3=df3[df3['Global_intensity'] <= 20.000]
    df3.to_csv('Global_intensity_19-20.csv', float_format='%.3f', index=0)
    df3=df3[df3['Sub_metering_2'] > df3['Sub_metering_3']]
    df3.to_csv('Sub_metering_2_more_sub_metering_3.csv', float_format='%.3f', index=0)
    randex=np.array(sample(range(len(df)), 500000))
    df4=df.ix[randex]
    df4.to_csv('Random_household_power_consumption.csv', float_format='%.3f', index=0)
    print ('DataFrame')
    print ('Mean of sub metering 1 for random data:',df4[['Sub_metering_1']].mean(axis=0)[0])
    print ('Mean of sub metering 2 for random data:',df4[['Sub_metering_2']].mean(axis=0)[0])
    print ('Mean of sub metering 3 for random data:',df4[['Sub_metering_3']].mean(axis=0)[0])
    df5=df[df['Time'] > '18:00:00']
    df5=df5[df5[['Global_active_power', 'Global_reactive_power']].mean(axis=1) > 2.000]
    df5.to_csv('Time_more_1800_avg_more_2.csv', float_format='%.3f', index=0)
    df5=df5[df5[['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']].max(axis=1) == df5['Sub_metering_2']]
    df5.to_csv('Sub_metering_2_max.csv', float_format='%.3f', index=0)
    df5.index=range(len(df5))
    half_size=len(df5)/2
    df5_1=df5.iloc[:half_size]
    df5_1=df5_1.iloc[::3, :]
    df5_1.to_csv('Every_3_1st_half.csv', float_format='%.3f')
    df5_2=df5.iloc[half_size:]
    df5_2=df5_2.iloc[::4, :]
    df5_2.to_csv('Every_4_2nd_half.csv', float_format='%.3f')
    
def array():
    txt_file="Clean_data.txt"
    ar=np.genfromtxt(txt_file, delimiter=',', names=True, dtype="|S15, |S15, float, float, float, float, float, float, float")
    ar1=ar[ar['Global_active_power'] > 5.000]
    s=','.join(ar.dtype.names)
    np.savetxt('arrGlobal_active_power_more_5.csv', ar1 , delimiter=',', fmt="%s,%s,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f", header=s, comments='')
    ar2=ar[ar['Voltage'] > 235.000]
    np.savetxt('arrVoltage_more_235.csv', ar2 , delimiter=',', fmt="%s,%s,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f", header=s, comments='')
    ar3=ar[ar['Global_intensity'] >= 19.000]
    ar3=ar3[ar3['Global_intensity'] <= 20.000]
    np.savetxt('arrGlobal_intensity_19-20.csv', ar3 , delimiter=',', fmt="%s,%s,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f", header=s, comments='')
    ar3=ar3[ar3['Sub_metering_2'] > ar3['Sub_metering_3']]
    np.savetxt('arrSub_metering_2_more_sub_metering_3.csv', ar3 , delimiter=',', fmt="%s,%s,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f", header=s, comments='')
    ar4=np.random.choice(ar, 500000, replace=False)
    np.savetxt('Random_household_power_consumption.csv', ar4 , delimiter=',', fmt="%s,%s,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f", header=s, comments='')
    print ('Numpy array')
    print ('Mean of sub metering 1 for random data:',np.mean(ar4['Sub_metering_1']))
    print ('Mean of sub metering 2 for random data:',np.mean(ar4['Sub_metering_2']))
    print ('Mean of sub metering 3 for random data:',np.mean(ar4['Sub_metering_3']))
    ar5=ar[ar['Time'] > '18:00:00']
    ar5=ar5[(ar5['Global_active_power']+ar5['Global_reactive_power'])/2 > 2.000]
    np.savetxt('arrTime_more_1800_avg_2.csv', ar5 , delimiter=',', fmt="%s,%s,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f", header=s, comments='')
    ar5=ar5[(ar5['Sub_metering_1'] <= ar5['Sub_metering_2']) & (ar5['Sub_metering_3'] <= ar5['Sub_metering_2'])]
    np.savetxt('arrSub_metering_2_max.csv', ar5 , delimiter=',', fmt="%s,%s,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f", header=s, comments='')
    half_size=len(ar5)/2
    ar5_1=ar5[:half_size]
    ar5_1=ar5_1[::3]
    np.savetxt('arrEvery_3_1st_half.csv', ar5_1 , delimiter=',', fmt="%s,%s,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f", header=s, comments='')
    ar5_2=ar5[half_size:]
    ar5_2=ar5_2[::4]
    np.savetxt('arrEvery_4_2nd_half.csv', ar5_2 , delimiter=',', fmt="%s,%s,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f", header=s, comments='')

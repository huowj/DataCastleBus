#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 13:50:18 2018

@author: root
"""

import os
import re
import math
import datetime
import time
import pandas as pd
import numpy as np
from scipy import stats
import pandas as pd

testdata0=pd.read_csv("/root/bus/dataset/seconds_passed.csv")

length_total = len(testdata0)

pred_time_list = []

for index in range(length_total):
    date = testdata0.O_DATA[index].split("-")[1]
    line = testdata0.O_LINENO[index]
    terminal = testdata0.O_TERMINALNO[index]
    hour = int(testdata0.predHour[index].split(":")[0])
    start_station = testdata0.pred_start_stop_ID[index]
    end_station = testdata0.pred_end_stop_ID[index]
    up = testdata0.O_UP[index]
    seconds = testdata0.seconds[index]
    intervals = range(start_station+1, end_station+2)
    word = "_" + str(line) + ".csv"
    df = pd.DataFrame(columns = ['no', 'interval', 'time'])
    date_used = []
    for j in range(5):
        date_j = int(date) - 7 * j
        if (date_j > 7 and date_j < 10):
            date_used.append('0' + str(date_j))
        elif (date_j >= 10):
            date_used.append(str(date_j))
    for i in date_used:
        file = "/root/bus/data_small/201710" + i + "_small"
        try:
            data_val = pd.read_csv(file + "/10" + i + "_" + str(line) + ".csv")
        except:
            continue
        data_val = data_val[data_val['O_UP'] == up]
        data_val = data_val[data_val['O_NEXTSTATIONNO'].isin(intervals)]
        data_val['hour'] = data_val.O_TIME.apply(lambda x: int(x.split(":")[0]))
        data_val = data_val[data_val['hour'] >= (hour-1)]
        data_val = data_val[data_val['hour'] <= (hour+1)]
        bus_list = list(set(data_val.O_TERMINALNO))
#        print(bus_list)
        for bus in bus_list:
            data_bus = data_val[data_val['O_TERMINALNO'] == bus]
            print(data_bus)
            if (data_bus.O_NEXTSTATIONNO.iloc[0] == start_station+1):
                start_time = datetime.datetime.strptime(data_bus.O_TIME.iloc[0],"%H:%M:%S")
            else:
                continue
            for p in range(1,len(data_bus)):
                if (data_bus.O_NEXTSTATIONNO.iloc[p] > data_bus.O_NEXTSTATIONNO.iloc[p-1]):
                    this_time = datetime.datetime.strptime(data_bus.O_TIME.iloc[p],"%H:%M:%S")
                    time_difference = (this_time - start_time).seconds
                    this_station=data_bus.O_NEXTSTATIONNO.iloc[p]-1
                    if time_difference > 3600:
                        break
                    row = pd.DataFrame({'no':[index],'interval':[this_station],"time":[time_difference]})
                    df = df.append(row, ignore_index = True)
    grouped = df['time'].astype(int).groupby(df['interval'])
    result = grouped.median()
    print(result)
    pred_time = ''
    for q in range(start_station + 1, end_station + 1):
        try:
            x = result[q]
        except:
            x += 128
        pred_time = pred_time + str(int(x)) + ";"
    pred_time = pred_time[:-1]
    print(index)
    print(pred_time)
    pred_time_list.append(pred_time)
    if ((index % 10) == 0):
        pred_time=pd.DataFrame(pred_time_list,columns=["pred_timeStamps"])
        pred_time.to_csv("/root/bus/predict.csv")
        
pred_timeStamps=pd.DataFrame(pred_time_list,columns=["without_first"])
predict_table=pd.concat([testdata0,pred_timeStamps],axis=1)
predict_table.to_csv("/root/bus/predict_without_first.csv",index=0)   

without_first = pd.read_csv("/hwj/bus/predict_without_first.csv")
first_station = pd.read_csv("/hwj/bus/first_station.csv")
testdata0=pd.read_csv("/hwj/bus/dataset/toBePredicted_forUser.csv")

time = []

for i in range(len(without_first)):
    a = [str(int(first_station.first_station_3[i]))]
    for item in without_first.without_first[i].split(";"):
        a.append(str(int(int(item)+first_station.first_station_3[i])))
    print(";".join(a))
    time.append(";".join(a))

pred_timeStamps=pd.DataFrame(time,columns=["pred_timeStamps"])
predict_table=pd.concat([without_first,pred_timeStamps],axis=1)
a = pd.merge(testdata0,predict_table)
a = a.drop(["O_UP","seconds","without_first"],axis = 1)
a.to_csv("/hwj/bus/predict_table_fs_4.csv", index = 0)

    
    
    
   
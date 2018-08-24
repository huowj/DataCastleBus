#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:00:56 2018

@author: hwj
"""

import pandas as pd
import numpy as np
import time
import datetime
from matplotlib import pyplot as plt

#testdata = pd.read_csv("/hwj/bus/dataset/toBePredicted_sorted.csv")
#
#len(set(testdata.O_LINENO))
##375
#
## line + up
#testdata["line_up"] = testdata["O_LINENO"].map(str) + "_" + testdata["O_UP"].map(str)
#len(set(testdata.line_up))
##700

seconds = pd.read_csv("/hwj/bus/dataset/seconds_passed.csv")
min_list = [-1]*len(seconds)
max_list = [-1]*len(seconds)
max_total_time = [-1]*len(seconds)
min_total_time = [-1]*len(seconds)
median_total_time = [-1]*len(seconds)
mean_total_time = [-1]*len(seconds)
list_25 = [-1] * len(seconds)
list_75 = [-1] * len(seconds)

for i in range(len(seconds)):
    print(seconds[i:i+1])
    date = seconds.O_DATA[i].split("-")[1]
    line = seconds.O_LINENO[i]
    terminal = seconds.O_TERMINALNO[i]
    predhour = seconds.predHour[i].split(":")[0]
    up = seconds.O_UP[i]
    file = "/hwj/bus/data_small/20171018_small/1018_" + str(line) + ".csv"
    try:
        data = pd.read_csv(file)
    except:
        continue
    data = data[data["O_UP"] == up]
    min_station = min(data.O_NEXTSTATIONNO)
    max_station = max(data.O_NEXTSTATIONNO)
    time_list = []
    flag = 0
    for j in range(len(data)-1):
        if data.O_NEXTSTATIONNO.iloc[j] == min_station:
            start_time = datetime.datetime.strptime(data.O_TIME.iloc[j],"%H:%M:%S")
            flag = 1
        if (flag == 1 and data.O_NEXTSTATIONNO.iloc[j] == max_station and data.O_NEXTSTATIONNO.iloc[j] > data.O_NEXTSTATIONNO.iloc[j+1]):
            end_time = datetime.datetime.strptime(data.O_TIME.iloc[j],"%H:%M:%S")
            total_time = (end_time - start_time).seconds
            time_list.append(total_time)
            start_time = datetime.datetime.strptime("0:0:0","%H:%M:%S")
            flag = 0
    min_list[i] = min_station
    max_list[i] = max_station
    if len(time_list) > 0:
        max_total_time[i] = max(time_list)
        min_total_time[i] = min(time_list)
        median_total_time[i] = np.median(time_list)
        mean_total_time[i] = np.mean(time_list)
        list_25[i] = np.percentile(time_list, 75)
        list_75[i] = np.percentile(time_list, 25)
#    plt.boxplot(time_list, whis=1.5)
#    plt.savefig("/hwj/bus/plot/" + str(line) + "_" + str(up) + ".jpg")
    
pred_timeStamps=pd.DataFrame({"mean" : mean_total_time, "median" : median_total_time, "min" : min_list, "max" : max_list, 
                              "maxtime" : max_total_time, "mintime" : min_total_time, "25" : list_25, "75" : list_75})
predict_table=pd.concat([seconds, pred_timeStamps],axis=1)
predict_table.to_csv("/hwj/bus/test_line.csv",index=0)      


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 22:03:38 2018

@author: hwj
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

testdata0=pd.read_csv("/hwj/bus/dataset/seconds_passed.csv")

length_total = len(testdata0)
mean_list = []
median_list = []
std_list = []
var_list = []
min_list = []
max_list = []
ptp_list = []

for index in range(28307, 28308):
    date = testdata0.O_DATA[index].split("-")[1]
    line = testdata0.O_LINENO[index]
    terminal = testdata0.O_TERMINALNO[index]
    hour = int(testdata0.predHour[index].split(":")[0])
    start_station = testdata0.pred_start_stop_ID[index]
    end_station = testdata0.pred_end_stop_ID[index]
    up = testdata0.O_UP[index]
    intervals = range(start_station, start_station + 2)
    df = pd.DataFrame(columns = ['no', 'interval', 'time'])
    date_used = []
    for j in range(5):
        date_j = int(date) - 7 * j
        if (date_j > 7 and date_j < 10):
            date_used.append('0' + str(date_j))
        elif (date_j >= 10):
            date_used.append(str(date_j))
    for i in date_used:
        file = "/hwj/bus/data_small/201710" + i + "_small"
        try:
            data_val = pd.read_csv(file + "/10" + i + "_" + str(line) + ".csv")
        except:
            continue
        data_val = data_val[data_val['O_UP'] == up]
        data_val = data_val[data_val['O_NEXTSTATIONNO'].isin(intervals)]
        data_val['hour'] = data_val.O_TIME.apply(lambda x: int(x.split(":")[0]))
        data_val = data_val[data_val['hour'] >= (hour - 1)]
        data_val = data_val[data_val['hour'] <= (hour + 1)]
        bus_list = list(set(data_val.O_TERMINALNO))
        for  bus in bus_list:
            data_bus = data_val[data_val['O_TERMINALNO'] == bus]
            hour_list = list(set(data_bus.hour))
            for hour0 in hour_list:
                data_bus_hour = data_bus[data_bus['hour'] == hour0]
                print(data_bus_hour)
                time_difference = 0
                if (len(data_bus_hour) > 0 and data_bus_hour.O_NEXTSTATIONNO.iloc[0] == start_station):
                    start_time = datetime.datetime.strptime(data_bus_hour.O_TIME.iloc[0],"%H:%M:%S")
                else:
                    continue
                for p in range(1,len(data_bus_hour)):
                    if (data_bus_hour.O_NEXTSTATIONNO.iloc[p] > data_bus_hour.O_NEXTSTATIONNO.iloc[p-1]):
                        this_time = datetime.datetime.strptime(data_bus_hour.O_TIME.iloc[p],"%H:%M:%S")
                        time_difference = (this_time - start_time).seconds
                        if (time_difference > 3600 or time_difference == 0):
                            break
                print(time_difference)
                row = pd.DataFrame({'no':[index],'interval':[start_station],"time":[time_difference]})
                df = df.append(row, ignore_index = True)
    median_list.append(df.time.median())
    mean_list.append(df.time.mean())
    var_list.append(df.time.var())
    std_list.append(df.time.std())
    min_list.append(df.time.min())
    max_list.append(df.time.max())
    ptp_list.append(df.time.ptp())
    
#pred_timeStamps=pd.DataFrame({"mean" : mean_list, "median" : median_list, "var" : var_list, "std" : std_list,
#                              "min" : min_list, "max" : max_list, "ptp" : ptp_list})
#predict_table=pd.concat([testdata0,pred_timeStamps],axis=1)
#predict_table.to_csv("/hwj/bus/first_station.csv",index=0)
            
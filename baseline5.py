#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 17:24:23 2018

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

testdata0 = pd.read_csv("/hwj/bus/dataset/toBePredicted_sorted.csv")

#testdata0 = testdata0.sort_values(by = ['O_DATA', 'O_LINENO', 'O_TERMINALNO', 'predHour'], 
#                                  axis = 0, ascending = True)
#testdata0 = testdata0.reset_index(drop = True)
#testdata0.to_csv("/root/bus/dataset/toBePredicted_sorted.csv", index = 0)

print(testdata0.head())

length_total = len(testdata0)

seconds = [-1] * length_total

stations = [-1] * length_total

for index in range(length_total):
    date = testdata0.O_DATA[index].split("-")[1] #str
    line = testdata0.O_LINENO[index]
    terminal = testdata0.O_TERMINALNO[index]
    hour = int(testdata0.predHour[index].split(":")[0])
    up = testdata0.O_UP[index]
    start_station = testdata0.pred_start_stop_ID[index]
    end_station = testdata0.pred_end_stop_ID[index]
    
    filename = "/hwj/bus/data_small/201710" + date + "_small"
    try:
        data_used = pd.read_csv(filename + "/10" + date + "_" + str(line) + ".csv")
    except:
        continue
    data_used = data_used[data_used['O_TERMINALNO']==terminal]
    data_used = data_used[data_used['O_UP']==up]
    data_used['hour'] = data_used.O_TIME.apply(lambda x: int(x.split(":")[0]))
    data_used = data_used[data_used['hour']==(hour -1)]
    time_1 = datetime.datetime.strptime(str(hour) + ":00:00", "%H:%M:%S")
    if (len(data_used)>1 and data_used.O_NEXTSTATIONNO.iloc[-2] == start_station):
        time_0 = datetime.datetime.strptime(data_used.O_TIME.iloc[-2], "%H:%M:%S")
        seconds_passed = (time_1-time_0).seconds
        station = 2
    elif (len(data_used)>0 and data_used.O_NEXTSTATIONNO.iloc[-1] == start_station):
        time_0 = datetime.datetime.strptime(data_used.O_TIME.iloc[-1], "%H:%M:%S")
        seconds_passed = (time_1-time_0).seconds
        station = 1
    elif (len(data_used) >0 and data_used.O_NEXTSTATIONNO.iloc[-1] == start_station-1):
        seconds_passed = 0
        station = 0
    seconds[index] = seconds_passed
    stations[index] = station
    print(index)

seconds = pd.DataFrame(seconds, columns = ['seconds'])
table = pd.concat([testdata0,seconds], axis = 1)
table.to_csv("/hwj/bus/dataset/seconds_passed.csv", index = 0)

    
        
        
        
    
    
    

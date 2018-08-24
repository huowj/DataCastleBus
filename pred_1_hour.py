#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:14:57 2018

@author: hwj
"""

import pandas as pd
import numpy as np
import time
import datetime
from matplotlib import pyplot as plt


seconds = pd.read_csv("/hwj/bus/dataset/seconds_passed.csv")

#min_list = [-1]*len(seconds)
#max_list = [-1]*len(seconds)
#
#
#test_25 = pd.DataFrame(columns=['O_LINENO', 'O_TERMINALNO', 'O_TIME',
#       'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED', 'O_MIDDOOR', 'O_REARDOOR',
#       'O_FRONTDOOR', 'O_UP', 'O_RUN', 'O_NEXTSTATIONNO', 'hour'])
#test_26 = pd.DataFrame(columns=['O_LINENO', 'O_TERMINALNO', 'O_TIME',
#       'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED', 'O_MIDDOOR', 'O_REARDOOR',
#       'O_FRONTDOOR', 'O_UP', 'O_RUN', 'O_NEXTSTATIONNO', 'hour'])
#test_27 = pd.DataFrame(columns=['O_LINENO', 'O_TERMINALNO', 'O_TIME',
#       'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED', 'O_MIDDOOR', 'O_REARDOOR',
#       'O_FRONTDOOR', 'O_UP', 'O_RUN', 'O_NEXTSTATIONNO', 'hour'])
#test_28 = pd.DataFrame(columns=['O_LINENO', 'O_TERMINALNO', 'O_TIME',
#       'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED', 'O_MIDDOOR', 'O_REARDOOR',
#       'O_FRONTDOOR', 'O_UP', 'O_RUN', 'O_NEXTSTATIONNO', 'hour'])
#test_29 = pd.DataFrame(columns=['O_LINENO', 'O_TERMINALNO', 'O_TIME',
#       'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED', 'O_MIDDOOR', 'O_REARDOOR',
#       'O_FRONTDOOR', 'O_UP', 'O_RUN', 'O_NEXTSTATIONNO', 'hour'])
#test_30 = pd.DataFrame(columns=['O_LINENO', 'O_TERMINALNO', 'O_TIME',
#       'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED', 'O_MIDDOOR', 'O_REARDOOR',
#       'O_FRONTDOOR', 'O_UP', 'O_RUN', 'O_NEXTSTATIONNO', 'hour'])
#test_31 = pd.DataFrame(columns=['O_LINENO', 'O_TERMINALNO', 'O_TIME',
#       'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED', 'O_MIDDOOR', 'O_REARDOOR',
#       'O_FRONTDOOR', 'O_UP', 'O_RUN', 'O_NEXTSTATIONNO', 'hour'])
#
#
#for i in range(1):
#    print(seconds[i:i+1])
#    date = seconds.O_DATA[i].split("-")[1]
#    line = seconds.O_LINENO[i]
#    terminal = seconds.O_TERMINALNO[i]
#    predhour = int(seconds.predHour[i].split(":")[0])
#    up = seconds.O_UP[i]
#    file = "/hwj/bus/data_transform/201710" + date + "/10" + date + "_" + str(line) + ".csv"
#    data = pd.read_csv(file)
#    data = data[data["O_TERMINALNO"] == terminal]
#    data = data[data["O_UP"] == up]
#    data["hour"] = data.O_TIME.apply(lambda x: int(x.split(":")[0]))
#    data = data[data["hour"] == predhour-1]
#    if len(data)<2:
#        continue
#    flag = [0] * len(data)
#    flag[0] = 1
#    flag[-1] = 1
#    for j in range(1,len(data)-1):
#        if (data.O_NEXTSTATIONNO.iloc[j] != data.O_NEXTSTATIONNO.iloc[j-1] or 
#            data.O_NEXTSTATIONNO.iloc[j] != data.O_NEXTSTATIONNO.iloc[j+1]):
#            flag[j] = 1
#    flag = pd.DataFrame(flag,columns=["flag"])
#    data = data.reset_index()
#    data = pd.concat([data,flag], axis = 1)
#    data = data[data["flag"] == 1].reset_index()
#    data = data[['O_LINENO', 'O_TERMINALNO', 'O_TIME',
#                 'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED', 'O_MIDDOOR', 'O_REARDOOR',
#                 'O_FRONTDOOR', 'O_UP', 'O_RUN', 'O_NEXTSTATIONNO', 'hour']]
#    if date == '25':
#        test_25 = test_25.append(data)
#    elif date == '26':
#        test_26 = test_26.append(data)
#    elif date == '27':
#        test_27 = test_27.append(data)
#    elif date == '28':
#        test_28 = test_28.append(data)
#    elif date == '29':
#        test_29 = test_29.append(data)
#    elif date == '30':
#        test_30 = test_30.append(data)
#    elif date == '31':
#        test_31 = test_31.append(data)
#
#
#test_25.to_csv("/hwj/bus/dataset/test_25.csv", index = 0)
#test_26.to_csv("/hwj/bus/dataset/test_26.csv", index = 0)
#test_27.to_csv("/hwj/bus/dataset/test_27.csv", index = 0)
#test_28.to_csv("/hwj/bus/dataset/test_28.csv", index = 0)
#test_29.to_csv("/hwj/bus/dataset/test_29.csv", index = 0)
#test_30.to_csv("/hwj/bus/dataset/test_30.csv", index = 0)
#test_31.to_csv("/hwj/bus/dataset/test_31.csv", index = 0)

times_list = [-1] * len(seconds)
stations_list = [-1] * len(seconds)
last_time = pd.DataFrame(columns = ['O_DATA', 'O_LINENO', 'O_TERMINALNO', 'O_TIME', 'O_LONGITUDE', 'O_LATITUDE',
       'O_SPEED', 'O_MIDDOOR', 'O_REARDOOR', 'O_FRONTDOOR', 'O_UP', 'O_RUN',
       'O_NEXTSTATIONNO', 'hour'])
seconds['hour'] = seconds.predHour.apply(lambda x: int(x.split(":")[0])-1)

for i in range(len(seconds)):
    print(seconds[i:i+1])
    date = seconds.O_DATA[i].split("-")[1]
    line = seconds.O_LINENO[i]
    terminal = seconds.O_TERMINALNO[i]
    predhour = int(seconds.predHour[i].split(":")[0])
    up = seconds.O_UP[i]
    file = "/hwj/bus/dataset/test_" + date + ".csv"
    data = pd.read_csv(file)
    data = data[data["O_LINENO"] == line]
    data = data[data["O_TERMINALNO"] == terminal]
    data = data[data["O_UP"] == up]
    data = data[data["hour"] == predhour-1]
    if len(data)<1:
        continue
    data['O_DATA'] = seconds.O_DATA[i]
    start_station = data.O_NEXTSTATIONNO.iloc[0]
    end_station = data.O_NEXTSTATIONNO.iloc[-1]
    start_index = 1
    start_time = datetime.datetime.strptime(data.O_TIME.iloc[0], "%H:%M:%S")
    if data.O_NEXTSTATIONNO.iloc[1] == start_station:
        start_index = 2
        start_time = datetime.datetime.strptime(data.O_TIME.iloc[1], "%H:%M:%S")
    stations = [str(start_station)]
    times = []
    for j in range(start_index, len(data)-1):
        if data.O_NEXTSTATIONNO.iloc[j] < data.O_NEXTSTATIONNO.iloc[j+1]:
            end_time = datetime.datetime.strptime(data.O_TIME.iloc[j], "%H:%M:%S")
            time_difference = (end_time - start_time).seconds
            stations.append(str(data.O_NEXTSTATIONNO.iloc[j]))
            times.append(str(time_difference))
            start_time = datetime.datetime.strptime(data.O_TIME.iloc[j], "%H:%M:%S")
    end_time = datetime.datetime.strptime(data.O_TIME.iloc[-1], "%H:%M:%S")
    time_difference = (end_time - start_time).seconds
    stations.append(str(data.O_NEXTSTATIONNO.iloc[-1]))
    times.append(str(time_difference))
    times_str = ";".join(times)
    stations_str = ";".join(stations)
    last_time = last_time.append(data.iloc[-1])
    times_list[i] = times_str
    stations_list[i] = stations_str

times_list = pd.DataFrame(times_list, columns = ["times_list"])
stations_list = pd.DataFrame(stations_list, columns = ["stations_list"])
valuable = pd.concat([seconds,times_list,stations_list], axis = 1)
valuable = pd.merge(valuable, last_time, how = "left")
valuable.to_csv("/hwj/bus/dataset/valuable.csv", index = 0)
            
            
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:58:33 2018

@author: hwj
"""

import pandas as pd
import numpy as np
import time
import datetime
from matplotlib import pyplot as plt

#valuable = pd.read_csv("/hwj/bus/dataset/valuable.csv")
#
#for i in range(len(valuable)):
#    stations_list = valuable.stations_list[i].split(";")
#    times_list = valuable.times_list[i].split(";")
#    stations = list(map(lambda x:int(x), stations_list))
#    times = list(map(lambda x:int(x), times_list))
#    if (len(stations) > 1 and stations[0]>stations[1]):
#        del(times[0])
#        del(stations[0])
#        stations_str = list(map(lambda x:str(x), stations))
#        times_str = list(map(lambda x:str(x), times))
#        valuable.stations_list[i] = ";".join(stations_str)
#        valuable.times_list[i] = ";".join(times_str)
#    print(i)
#    
#valuable.to_csv("/hwj/bus/dataset/value.csv", index = 0)

value = pd.read_csv("/hwj/bus/dataset/value.csv")

dic = {"25" : ["18", "11"],
       "26" : ["19", "12"],
       "27" : ["20", "13"],
       "28" : ["21", "14"],
       "29" : ["22", "15"],
       "30" : ["23", "16", "9"],
       "31" : ["24", "17", "10"]}

file_dic = {"25" : "/hwj/bus/dataset/value_25.csv",
            "26" : "/hwj/bus/dataset/value_26.csv",
            "27" : "/hwj/bus/dataset/value_27.csv",
            "28" : "/hwj/bus/dataset/value_28.csv",
            "29" : "/hwj/bus/dataset/value_29.csv",
            "30" : "/hwj/bus/dataset/value_30.csv",
            "31" : "/hwj/bus/dataset/value_31.csv"}


value_25 = pd.DataFrame(columns = ['O_DATA', 'O_LINENO', 'O_TERMINALNO', 'predHour', 'pred_start_stop_ID',
       'pred_end_stop_ID', 'O_UP', 'seconds', 'stations', 'hour', 'times_list',
       'stations_list', 'O_TIME', 'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED',
       'O_MIDDOOR', 'O_REARDOOR', 'O_FRONTDOOR', 'O_RUN', 'O_NEXTSTATIONNO', 
       'R_O_LINENO', 'R_O_TERMINALNO', 'R_O_TIME', 'R_O_LONGITUDE', 'R_O_LATITUDE',
       'R_O_SPEED', 'R_O_MIDDOOR', 'R_O_REARDOOR', 'R_O_FRONTDOOR', 'R_O_UP', 'R_O_RUN',
       'R_O_NEXTSTATIONNO', 'R_loop_list', 'pre_times', 'pre_stations', 'pro_times', 'pro_stations'])
value_26 = pd.DataFrame(columns = ['O_DATA', 'O_LINENO', 'O_TERMINALNO', 'predHour', 'pred_start_stop_ID',
       'pred_end_stop_ID', 'O_UP', 'seconds', 'stations', 'hour', 'times_list',
       'stations_list', 'O_TIME', 'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED',
       'O_MIDDOOR', 'O_REARDOOR', 'O_FRONTDOOR', 'O_RUN', 'O_NEXTSTATIONNO', 
       'R_O_LINENO', 'R_O_TERMINALNO', 'R_O_TIME', 'R_O_LONGITUDE', 'R_O_LATITUDE',
       'R_O_SPEED', 'R_O_MIDDOOR', 'R_O_REARDOOR', 'R_O_FRONTDOOR', 'R_O_UP', 'R_O_RUN',
       'R_O_NEXTSTATIONNO', 'R_loop_list', 'pre_times', 'pre_stations', 'pro_times', 'pro_stations'])
value_27 = pd.DataFrame(columns = ['O_DATA', 'O_LINENO', 'O_TERMINALNO', 'predHour', 'pred_start_stop_ID',
       'pred_end_stop_ID', 'O_UP', 'seconds', 'stations', 'hour', 'times_list',
       'stations_list', 'O_TIME', 'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED',
       'O_MIDDOOR', 'O_REARDOOR', 'O_FRONTDOOR', 'O_RUN', 'O_NEXTSTATIONNO', 
       'R_O_LINENO', 'R_O_TERMINALNO', 'R_O_TIME', 'R_O_LONGITUDE', 'R_O_LATITUDE',
       'R_O_SPEED', 'R_O_MIDDOOR', 'R_O_REARDOOR', 'R_O_FRONTDOOR', 'R_O_UP', 'R_O_RUN',
       'R_O_NEXTSTATIONNO', 'R_loop_list', 'pre_times', 'pre_stations', 'pro_times', 'pro_stations'])
value_28 = pd.DataFrame(columns = ['O_DATA', 'O_LINENO', 'O_TERMINALNO', 'predHour', 'pred_start_stop_ID',
       'pred_end_stop_ID', 'O_UP', 'seconds', 'stations', 'hour', 'times_list',
       'stations_list', 'O_TIME', 'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED',
       'O_MIDDOOR', 'O_REARDOOR', 'O_FRONTDOOR', 'O_RUN', 'O_NEXTSTATIONNO', 
       'R_O_LINENO', 'R_O_TERMINALNO', 'R_O_TIME', 'R_O_LONGITUDE', 'R_O_LATITUDE',
       'R_O_SPEED', 'R_O_MIDDOOR', 'R_O_REARDOOR', 'R_O_FRONTDOOR', 'R_O_UP', 'R_O_RUN',
       'R_O_NEXTSTATIONNO', 'R_loop_list', 'pre_times', 'pre_stations', 'pro_times', 'pro_stations'])
value_29 = pd.DataFrame(columns = ['O_DATA', 'O_LINENO', 'O_TERMINALNO', 'predHour', 'pred_start_stop_ID',
       'pred_end_stop_ID', 'O_UP', 'seconds', 'stations', 'hour', 'times_list',
       'stations_list', 'O_TIME', 'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED',
       'O_MIDDOOR', 'O_REARDOOR', 'O_FRONTDOOR', 'O_RUN', 'O_NEXTSTATIONNO', 
       'R_O_LINENO', 'R_O_TERMINALNO', 'R_O_TIME', 'R_O_LONGITUDE', 'R_O_LATITUDE',
       'R_O_SPEED', 'R_O_MIDDOOR', 'R_O_REARDOOR', 'R_O_FRONTDOOR', 'R_O_UP', 'R_O_RUN',
       'R_O_NEXTSTATIONNO', 'R_loop_list', 'pre_times', 'pre_stations', 'pro_times', 'pro_stations'])
value_30 = pd.DataFrame(columns = ['O_DATA', 'O_LINENO', 'O_TERMINALNO', 'predHour', 'pred_start_stop_ID',
       'pred_end_stop_ID', 'O_UP', 'seconds', 'stations', 'hour', 'times_list',
       'stations_list', 'O_TIME', 'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED',
       'O_MIDDOOR', 'O_REARDOOR', 'O_FRONTDOOR', 'O_RUN', 'O_NEXTSTATIONNO', 
       'R_O_LINENO', 'R_O_TERMINALNO', 'R_O_TIME', 'R_O_LONGITUDE', 'R_O_LATITUDE',
       'R_O_SPEED', 'R_O_MIDDOOR', 'R_O_REARDOOR', 'R_O_FRONTDOOR', 'R_O_UP', 'R_O_RUN',
       'R_O_NEXTSTATIONNO', 'R_loop_list', 'pre_times', 'pre_stations', 'pro_times', 'pro_stations'])
value_31 = pd.DataFrame(columns = ['O_DATA', 'O_LINENO', 'O_TERMINALNO', 'predHour', 'pred_start_stop_ID',
       'pred_end_stop_ID', 'O_UP', 'seconds', 'stations', 'hour', 'times_list',
       'stations_list', 'O_TIME', 'O_LONGITUDE', 'O_LATITUDE', 'O_SPEED',
       'O_MIDDOOR', 'O_REARDOOR', 'O_FRONTDOOR', 'O_RUN', 'O_NEXTSTATIONNO', 
       'R_O_LINENO', 'R_O_TERMINALNO', 'R_O_TIME', 'R_O_LONGITUDE', 'R_O_LATITUDE',
       'R_O_SPEED', 'R_O_MIDDOOR', 'R_O_REARDOOR', 'R_O_FRONTDOOR', 'R_O_UP', 'R_O_RUN',
       'R_O_NEXTSTATIONNO', 'R_loop_list', 'pre_times', 'pre_stations', 'pro_times', 'pro_stations'])


for i in range(len(value)):
    date = value.O_DATA[i].split("-")[1]
    line = value.O_LINENO[i]
    terminal = value.O_TERMINALNO[i]
    up = value.O_UP[i]
    hour = int(value.predHour[i].split(":")[0])
    start_station = int(value.stations_list[i].split(";")[0])
    pred_start_station = value.pred_start_stop_ID[i]
    pred_end_station = value.pred_end_stop_ID[i]
    next_station = value.O_NEXTSTATIONNO[i]
    longitude = value.O_LONGITUDE[i]
    latitude = value.O_LATITUDE[i]
    vec = np.array([longitude,latitude])
    stations_list = value.stations_list[i].split(";")
    stations = list(map(lambda x:int(x), stations_list))
    for j in dic[date]:
        file = "/hwj/bus/data_transform/201710" + j + "/10" + j + "_" + str(line) + ".csv"
        data = pd.read_csv(file)
        data = data[data["O_UP"] == up]
        data["hour"] = data.O_TIME.apply(lambda x: int(x.split(":")[0]))
        data = data[data["hour"].isin(range(hour-2, hour+3))]
        data = data[data["O_NEXTSTATIONNO"].isin(range(start_station, pred_end_station+2))]
        bus_list = list(set(data.O_TERMINALNO))
        for bus in bus_list:
            data_bus = data[data["O_TERMINALNO"] == bus].iloc[:,1:13].reset_index(drop = True)
            loop_list = [0] * len(data_bus)
            loop = 0
            for p in range(1,len(data_bus)):
                if data_bus.O_NEXTSTATIONNO[p]<data_bus.O_NEXTSTATIONNO[p-1]:
                    loop += 1
                loop_list[p] = loop
            loop_list = pd.DataFrame(loop_list,columns=["loop_list"])
            data_bus = pd.concat([data_bus,loop_list],axis=1)
            for q in list(set(data_bus.loop_list)):
                data_bus_loop = data_bus[data_bus["loop_list"] == q].reset_index(drop = True)
                data_used = data_bus_loop[data_bus_loop["O_NEXTSTATIONNO"] == next_station]
                if (len(data_used) == 0):
                    continue
                best_index = data_used.index[0]
                dis = np.linalg.norm(vec - np.array(data_used.loc[best_index,'O_LONGITUDE':'O_LATITUDE']))
                for m in data_used.index:
                    if dis > np.linalg.norm(vec - np.array(data_used.loc[m,'O_LONGITUDE':'O_LATITUDE'])):
                        dis = np.linalg.norm(vec - np.array(data_used.loc[m,'O_LONGITUDE':'O_LATITUDE']))
                        best_index = m
                pre_stations = [str(data_bus_loop.O_NEXTSTATIONNO[0])]
                pre_times = []
                for n in range(best_index):
                    if data_bus_loop.O_NEXTSTATIONNO[n] == data_bus_loop.O_NEXTSTATIONNO[0]:
                        start_time = datetime.datetime.strptime(data_bus_loop.O_TIME[n], "%H:%M:%S")
                        continue
                    if (data_bus_loop.O_NEXTSTATIONNO[n] >= data_bus_loop.O_NEXTSTATIONNO[0] and 
                        data_bus_loop.O_NEXTSTATIONNO[n] < data_bus_loop.O_NEXTSTATIONNO[n+1]):
                        end_time = datetime.datetime.strptime(data_bus_loop.O_TIME[n], "%H:%M:%S")
                        time_difference = (end_time - start_time).seconds
                        pre_times.append(str(time_difference))
                        pre_stations.append(str(data_bus_loop.O_NEXTSTATIONNO[n]))
                        start_time = datetime.datetime.strptime(data_bus_loop.O_TIME.iloc[n], "%H:%M:%S")
                end_time = datetime.datetime.strptime(data_bus_loop.O_TIME.iloc[best_index], "%H:%M:%S")
                time_difference = (end_time - start_time).seconds
                pre_times.append(str(time_difference))
                pre_stations.append(str(data_bus_loop.O_NEXTSTATIONNO[best_index]))
                pre_times = ";".join(pre_times)
                pre_stations = ";".join(pre_stations)
                pro_times = []
                pro_stations = []
                start_time = datetime.datetime.strptime(data_bus_loop.O_TIME.iloc[best_index], "%H:%M:%S")
                for l in range(best_index+1,len(data_bus_loop)):
                    if data_bus_loop.O_NEXTSTATIONNO[l] > data_bus_loop.O_NEXTSTATIONNO[l-1]:
                        end_time = datetime.datetime.strptime(data_bus_loop.O_TIME.iloc[l], "%H:%M:%S")
                        time_difference = (end_time - start_time).seconds
                        pro_times.append(str(time_difference))
                        pro_stations.append(str(data_bus_loop.O_NEXTSTATIONNO[l]-1))
                pro_times = ";".join(pro_times)
                pro_stations = ";".join(pro_stations)
                R = pd.DataFrame([data_bus_loop.loc[best_index]]).reset_index(drop = True).rename(columns={
                        'O_LINENO' : 'R_O_LINENO', 'O_TERMINALNO' : 'R_O_TERMINALNO', 'O_TIME' : 'R_O_TIME', 
                        'O_LONGITUDE' : 'R_O_LONGITUDE', 'O_LATITUDE' : 'R_O_LATITUDE', 'O_SPEED' : 'R_O_SPEED', 
                        'O_MIDDOOR' : 'R_O_MIDDOOR', 'O_REARDOOR' : 'R_O_REARDOOR', 'O_FRONTDOOR' : 'R_O_FRONTDOOR', 
                        'O_UP' : 'R_O_UP', 'O_RUN' : 'R_O_RUN', 'O_NEXTSTATIONNO' : 'R_O_NEXTSTATIONNO', 
                        'loop_list' : 'R_loop_list'})
                L = pd.DataFrame([value.loc[i]]).reset_index(drop = True)
                M = pd.DataFrame.from_dict({'pre_stations' : pre_stations,
                                            'pre_times' : pre_times,
                                            'pro_stations' : pro_stations,
                                            'pro_times' : pro_times},orient='index').T
                T = pd.concat([L,R,M],axis=1)
                if date == '25':
                    value_25 = value_25.append(T)
                elif date == '26':
                    value_26 = value_26.append(T)
                elif date == '27':
                    value_27 = value_27.append(T)
                elif date == '28':
                    value_28 = value_28.append(T)
                elif date == '29':
                    value_29 = value_29.append(T)
                elif date == '30':
                    value_30 = value_30.append(T)
                elif date == '31':
                    value_31 = value_31.append(T)
    if date == '25':
        value_25.to_csv(file_dic["25"], index = 0)
    elif date == '26':
        value_26.to_csv(file_dic["26"], index = 0)
    elif date == '27':
        value_27.to_csv(file_dic["27"], index = 0)
    elif date == '28':
        value_28.to_csv(file_dic["28"], index = 0)
    elif date == '29':
        value_29.to_csv(file_dic["29"], index = 0)
    elif date == '30':
        value_30.to_csv(file_dic["30"], index = 0)
    elif date =='31':
        value_31.to_csv(file_dic["31"], index = 0)
    print(i)
                
                
                        
                    
                
                        
                
            
        

    
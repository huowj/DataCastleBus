#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 31 21:06:07 2018

@author: hwj
"""

import pandas as pd
import numpy as np

value_31 = pd.read_csv("/hwj/bus/value_31.csv")
value_31 = value_31.fillna(-1)

#l_stations = value_31.stations_list[3]
#l_times = value_31.times_list[3]
#r_stations = value_31.pre_stations[3]
#r_times = value_31.pre_times[3]

# left is the test set; right is the train set
def dist_cal(l, r):
    if (len(l) == len(r)):
        denominator = 0 #fenmu
        numerator = 0 #fenzi
        for n in range(len(l)):
            denominator += (np.square(l[n]) + np.square(r[n]) - (l[n]*r[n]))
            numerator += (l[n]*r[n])
        if (denominator != 0):
            dist = numerator/denominator
        else:
            return(0)
    return(dist)
#
#l_station_list = [int(x) for x in l_stations.split(";")]
#l_time_list = [int(x) for x in l_times.split(";")]
#r_station_list = [int(x) for x in r_stations.split(";")]
#r_time_list = [int(x) for x in r_times.split(";")]
#intersection = list(set(l_station_list).intersection(set(r_station_list)))
#
#l_time_t = []
#r_time_t = []
#for i in range(len(intersection) - 1):
#    start = intersection[i]
#    end = intersection[i+1]
#    l_start_index = l_station_list.index(start)
#    l_end_index = l_station_list.index(end)
#    l_dif = l_end_index - l_start_index
#    r_start_index = r_station_list.index(start)
#    r_end_index = r_station_list.index(end)
#    r_dif = r_end_index - r_start_index
#    l_time = 0
#    for j in range(l_dif):
#        l_time += l_time_list[l_start_index + j]
#    l_time_t.append(l_time)
#    r_time = 0
#    for k in range(r_dif):
#        r_time += r_time_list[r_start_index + k]
#    r_time_t.append(r_time)
#
#print(dist_cal(l_time_t, r_time_t))


dist_list = [-1] * len(value_31)
for p in range(len(value_31)):
    l_stations = value_31.stations_list[p]
    l_times = value_31.times_list[p]
    r_stations = value_31.pre_stations[p]
    r_times = value_31.pre_times[p]
    if(l_times == -1):
        continue
    l_station_list = [int(x) for x in l_stations.split(";")]
    l_time_list = [int(x) for x in l_times.split(";")]
    r_station_list = [int(x) for x in r_stations.split(";")]
    r_time_list = [int(x) for x in r_times.split(";")]
    intersection = list(set(l_station_list).intersection(set(r_station_list)))
    
    l_time_t = []
    r_time_t = []
    for i in range(len(intersection) - 1):
        start = intersection[i]
        end = intersection[i+1]
        l_start_index = l_station_list.index(start)
        l_end_index = l_station_list.index(end)
        l_dif = l_end_index - l_start_index
        r_start_index = r_station_list.index(start)
        r_end_index = r_station_list.index(end)
        r_dif = r_end_index - r_start_index
        l_time = 0
        for j in range(l_dif):
            l_time += l_time_list[l_start_index + j]
        l_time_t.append(l_time)
        r_time = 0
        for k in range(r_dif):
            r_time += r_time_list[r_start_index + k]
        r_time_t.append(r_time)
    
    dist_list[p] = dist_cal(l_time_t, r_time_t)
    print("index :", p, dist_cal(l_time_t, r_time_t))

dist_list = pd.DataFrame(dist_list,columns=["dist"])
value_31 = pd.concat([value_31, dist_list],axis=1)
value_31 = value_31.sort_values(['O_DATA', 'O_LINENO', 'O_TERMINALNO', 'predHour', 'dist'], 
                                ascending = [True, True, True, True, False])
value_31.to_csv("/hwj/bus/value_31_0.csv", index = 0)
    
    


















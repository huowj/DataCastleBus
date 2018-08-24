#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:29:47 2018

@author: root
"""

import pandas as pd
import numpy as np
from scipy.interpolate import lagrange

predict = pd.read_csv("/root/bus/dataset/toBePredicted_sorted.csv")

k = 5

res = [-1] * len(predict)
attention = []

for i in range(len(predict)):
    date = predict.O_DATA.iloc[i].split("-")[1]
    line = predict.O_LINENO.iloc[i]
    terminal = predict.O_TERMINALNO.iloc[i]
    hour = predict.predHour.iloc[i]
    start_station = predict.pred_start_stop_ID.iloc[i]
    end_station = predict.pred_end_stop_ID.iloc[i]
    pre_stations = range(start_station, end_station + 1)
    up = predict.O_UP.iloc[i]
    data = pd.read_csv("/root/bus/dataset/value_" + date + "_0.csv")
    data_used = data[(data["O_LINENO"] == line) & 
                     (data["O_TERMINALNO"] == terminal) & 
                     (data["predHour"] == hour) & 
                     (data["O_UP"] == up)].reset_index(drop = True)
    k_data = data_used.iloc[0:k]
    if len(k_data) == 0:
        continue
    if k_data.dist.iloc[0] == 1:
        continue
    stations = []
    times = []
    for j in range(len(k_data)):
        s_list = k_data.pro_stations.iloc[j].split(";")
        stations.extend(list(map(lambda x:int(x), s_list)))
        t_list = k_data.pro_times.iloc[j].split(";")
        times.extend(list(map(lambda x:int(x), t_list)))
    t_data = pd.DataFrame.from_dict({'stations' : stations, 'times' : times},orient='index').T
    grouped = t_data['times'].astype(int).groupby(t_data['stations'])
    result = grouped.median()
    result_else = grouped.median().reset_index()
    dif = list(set(pre_stations) - set(result_else.stations))
    if (len(dif) > 0):
        print("attention", i)
        attention.append(i)
    pred_time = ''
    for q in pre_stations:
        try:
            x = result[q]
        except:
            x += 128
        pred_time = pred_time + str(int(x)) + ";"
    pred_time = pred_time[:-1]
    print(i, pred_time)
    res[i] = pred_time

pred_timeStamps=pd.DataFrame(res,columns=["result"])
predict_table=pd.concat([predict,pred_timeStamps],axis=1)
predict_table.to_csv("/root/bus/dataset/knn_test.csv",index=0)
attention = pd.DataFrame.from_dict({'attention' : attention},orient='index').T
attention.to_csv("/root/bus/dataset/attention.csv", index = 0)

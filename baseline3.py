#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 10:21:41 2018

@author: hwj
"""

"""
firstly find the starttime 
assume the time is the mean time of the first pred station
then calculate the difference
calculate the mean
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

testdata0=pd.read_csv("/hwj/bus/dataset/toBePredicted_forUser.csv")
testdata1=testdata0.drop('O_UP',1)

#print(testdata0.head(4))
#print(testdata1.head(4))
#
#for i in range(len(testdata0)):
#    for j in range(6):
#        a=testdata0.iloc[i,j]
#        b=testdata1.iloc[i,j]
#        if a!=b:
#            print([i,j])
############so these datasets are identical###########################
length_total=len(testdata0)
pred_time_list=[]
   

for index in range(1):
    date=testdata0.O_DATA[index].split("-")[1]
    line=testdata0.O_LINENO[index]
    terminal=testdata0.O_TERMINALNO[index]
    pred_hour=int(testdata0.predHour[index].split(":")[0])
    start_station=testdata0.pred_start_stop_ID[index]
    end_station=testdata0.pred_end_stop_ID[index]
    up=testdata0.O_UP[index]
    intervals=range(start_station,end_station+2)
    word="_"+str(line)+".csv"
    df = pd.DataFrame(columns = ['no','interval','time'])
#    print(pred_hour,date)
#    date_used=[str(int(date)-7)]
    date_used=[]
    for jj in range(5):
        date_jj=int(date)-7*jj
        if (date_jj>7 and date_jj<10):
            date_used.append('0'+str(date_jj))
        elif (date_jj>=10):
            date_used.append(str(date_jj))
#    date_used=['21']
#    print(date_used)
    for i in date_used:
        file="/hwj/bus/data_small/201710"+i+"_small"
#        print(file)
        filelist=os.listdir(file)
        for f in filelist:
            if word in f:
                data_used=pd.read_csv(file+"/"+f)
#                print(data_used.head())
                length_used=len(data_used)
                hour=[]
                for j in range(length_used):
                    hour.append(int(data_used.O_TIME.iloc[j].split(":")[0]))
#                print(hour)
                data_used.insert(5,"hour",hour)
#                print(data_used.head(3))
                d0=data_used[data_used['O_NEXTSTATIONNO'].isin(intervals)]
                d1=d0[d0['O_UP']==up]
                d2=d1[d1['hour']>=(pred_hour-1)]
                d3=d2[d2['hour']<=(pred_hour+1)]
#                print(d3.head())
#                d3.to_csv("/hwj/busd3.csv")
                bus_list=list(set(d3.O_TERMINALNO))
#                print(bus_list)
                for bus in bus_list:
                    data_bus=d3[d3['O_TERMINALNO']==bus]
                    if(len(data_bus)<10):
                        continue
                    zero=data_bus.O_NEXTSTATIONNO.iloc[0]
                    one=data_bus.O_NEXTSTATIONNO.iloc[1]
                    if (zero==one and zero==start_station):
                        zero_time=datetime.datetime.strptime(data_bus.O_TIME.iloc[0],"%H:%M:%S")
                        one_time=datetime.datetime.strptime(data_bus.O_TIME.iloc[1],"%H:%M:%S")
#                        print(zero_time)
                        delta_seconds=(one_time-zero_time).seconds
#                        print(delta_seconds)
                        mean_time=zero_time+datetime.timedelta(seconds = int((delta_seconds)/2))
#                        print(bus,mean_time)
                    else:
#                        mean_time=datetime.datetime.strptime(data_bus.O_TIME.iloc[0],"%H:%M:%S")
                        continue
                    for another_index in range(1,len(data_bus)):
                        if (data_bus.O_NEXTSTATIONNO.iloc[another_index]>data_bus.O_NEXTSTATIONNO.iloc[another_index-1]):
                            this_time=datetime.datetime.strptime(data_bus.O_TIME.iloc[another_index],"%H:%M:%S")
                            time_difference=(this_time-mean_time).seconds
                            this_station=data_bus.O_NEXTSTATIONNO.iloc[another_index]-1
                            if time_difference>3600:
                                break
#                            print(this_station,time_difference)
                            row = pd.DataFrame({'no':[index],'interval':[this_station],"time":[time_difference]})
                            df=df.append(row,ignore_index=True)
    grouped=df['time'].astype(int).groupby(df['interval'])
    result=grouped.median()
    print(result)
    pred_time=''
    for p in range(start_station,end_station+1):
        try:
            x=result[p]
        except:
            x+=128
        pred_time=pred_time+str(int(x))+";"
    pred_time=pred_time[:-1]
    print(index)
    print(pred_time)
    pred_time_list.append(pred_time)  

#pred_timeStamps=pd.DataFrame(pred_time_list,columns=["pred_timeStamps"])
#predict_table=pd.concat([testdata1,pred_timeStamps],axis=1)
#predict_table.to_csv("/hwj/bus/predict_table_lll2.csv",index=0)

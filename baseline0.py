#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 21:13:16 2018

@author: hwj
"""
import os
import re
import math
import datetime
import time
import pandas as pd
import numpy as np

import pandas as pd

testdata=pd.read_csv("/hwj/bus/toBePredicted_update_0523.csv")

#line=testdata.O_LINENO[0]
#bus=testdata.O_TERMINALNO[0]
#start_station=testdata.pred_start_stop_ID[0]
#end_station=testdata.pred_end_stop_ID[0]
#
#for l in range(10):
#    loop=l+1
#    if loop<10:
#        loop_str="0"+str(loop)
#    else:
#        loop_str=str(loop)
#    file="/hwj/bus/data_interval/201710"+loop_str+"_interval"
#    word="_"+str(line)+".csv"
#    filelist=os.listdir(file)
#    for f in filelist:
#        if word in f:
#            data=pd.read_csv(file+"/"+f)
#            print(file+"/"+f)
#            print(data.head(2))
            
length=len(testdata)
pred_time_list=[]

for index in range(length):
    print(index)
    line=testdata.O_LINENO[index]
    bus=testdata.O_TERMINALNO[index]
    up=testdata.O_UP[index]
    start_station=testdata.pred_start_stop_ID[index]
    end_station=testdata.pred_end_stop_ID[index]
    predhour=testdata.predHour[index]
    date=datetime.datetime.strptime("2017-"+testdata.O_DATA[index],"%Y-%m-%d")
    word="_"+str(line)+".csv"
    intervals=range(start_station-1,end_station)
    print(intervals)
    df = pd.DataFrame(columns = ['O_LINENO', 'O_TERMINALNO', 'O_TIME', 'O_UP', 'O_NEXTSTATIONNO', 'interval', 'mean_time', 'interval_time', 'weekday'])
    for i in range(18,25):
        file="/hwj/bus/data_interval/201710"+str(i)+"_interval"
        filelist=os.listdir(file)
        for f in filelist:
            if word in f:
                data=pd.read_csv(file+"/"+f)
#                print(file+"/"+f)
#                print(data.head(2))
                d0=data[data['interval'].isin(intervals)]
                d1=d0[d0['O_UP']==up]
                df=pd.concat([df,d1],ignore_index=True)
    grouped=df['interval_time'].astype(int).groupby(df['interval'])
    result=grouped.mean()
#    print(result)
    try:
        x=result[start_station-1]/2
    except:
        x=64
#    print(x)
    pred_time=str(int(x))+";"
#    print(pred_time)
    for p in range(start_station,end_station):
        try:
            x+=result[p]
        except:
            x+=128
        pred_time=pred_time+str(int(x))+";"
    pred_time=pred_time[:-1]
    print(pred_time)
    pred_time_list.append(pred_time)
#    print(pred_time_list)



pred_timeStamps=pd.DataFrame(pred_time_list,columns=["pred_timeStamps"])
predict_table=pd.concat([testdata,pred_timeStamps],axis=1)
predict_table.to_csv("/hwj/bus/predict_table_0.csv",index=0)
    
        
        
                
                    
                
  




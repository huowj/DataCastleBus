#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:50:36 2018

@author: hwj
"""

import os
import re
import math
import datetime
import time
import pandas as pd
import numpy as np



#day=pd.read_csv("/hwj/bus/data_small/20171001_small/1001_813.csv")
#length=len(day)
#print(length)
#
#today=datetime.datetime.strptime("2017-10-01","%Y-%m-%d")
#
#interval=[-1]*length
#mean_time=[-1]*length
#interval_time=[-1]*length
#weekday=[today.weekday()]*length
#mean_time[0]=day.O_TIME[0]
#mean_time[length-1]=day.O_TIME[length-1]
#
#for i in range(2,length):
#    now_next=day.O_NEXTSTATIONNO[i-1]
#    now_pre=day.O_NEXTSTATIONNO[i-2]
#    now_time=datetime.datetime.strptime("2017-10-01 "+day.O_TIME[i],"%Y-%m-%d %H:%M:%S")
#    now_pre_time=datetime.datetime.strptime("2017-10-01 "+day.O_TIME[i-1],"%Y-%m-%d %H:%M:%S")
#    delta_seconds=(now_time-now_pre_time).seconds
#    mean_time[i-1]=now_pre_time+datetime.timedelta(seconds = int((delta_seconds)/2))
#    if now_next!=now_pre:
#        interval[i]=now_next-1
#
##for j in range(2,length-1):
##    if interval[j]!=(-1):
##        interval_time[j]=(mean_time[j]-mean_time[j-2]).seconds
#    
#
#day.insert(5,"interval",interval)
#day.insert(6,"mean_time",mean_time)
#day.insert(7,"interval_time",interval_time)
#day.insert(8,"weekday",weekday)
#day.to_csv("/hwj/bus/interval_1001_3.csv",index=0)


#############for loop###################
for l in range(17,24):
    loop=l+1
    if loop<10:
        loop_str="0"+str(loop)
    else:
        loop_str=str(loop)
    os.mkdir("/hwj/bus/data_interval/201710"+loop_str+"_interval")
    file="/hwj/bus/data_small/201710"+loop_str+"_small"
    filelist=os.listdir(file)
    for f in filelist:
        if os.path.splitext(f)[1] != '.csv':
            break
        print(f)
        day=pd.read_csv("/hwj/bus/data_small/201710"+loop_str+"_small/"+f)
        length=len(day)
        print(length)

        today=datetime.datetime.strptime("2017-10-"+loop_str,"%Y-%m-%d")
        hour=[-1]*length
        interval=[-1]*length
        mean_time=[-1]*length
        interval_time=[-1]*length
        weekday=[today.weekday()]*length
        mean_time[0]=datetime.datetime.strptime("2017-10-"+loop_str+" "+day.O_TIME[0],"%Y-%m-%d %H:%M:%S")
        mean_time[length-1]=datetime.datetime.strptime("2017-10-"+loop_str+" "+day.O_TIME[length-1],"%Y-%m-%d %H:%M:%S")
        hour[0]=mean_time[0].hour
        hour[-1]=mean_time[-1].hour

        for i in range(2,length):
            now_next=day.O_NEXTSTATIONNO[i-1]
            now_pre=day.O_NEXTSTATIONNO[i-2]
            now_time=datetime.datetime.strptime("2017-10-"+loop_str+" "+day.O_TIME[i],"%Y-%m-%d %H:%M:%S")
            now_pre_time=datetime.datetime.strptime("2017-10-"+loop_str+" "+day.O_TIME[i-1],"%Y-%m-%d %H:%M:%S")
            delta_seconds=(now_time-now_pre_time).seconds
            mean_time[i-1]=now_pre_time+datetime.timedelta(seconds = int((delta_seconds)/2))
            hour[i-1]=mean_time[i-1].hour
            if now_next!=now_pre:
                interval[i]=now_next-1

        for j in range(2,length-1):
            if interval[j]!=(-1):
                interval_time[j]=(mean_time[j]-mean_time[j-2]).seconds
    

        day.insert(5,"interval",interval)
        day.insert(6,"mean_time",mean_time)
        day.insert(7,"interval_time",interval_time)
        day.insert(8,"weekday",weekday)
        day.insert(9,"hour",hour)
        day.to_csv("/hwj/bus/data_interval/201710"+loop_str+"_interval/"+f,index=0)
        
    
    

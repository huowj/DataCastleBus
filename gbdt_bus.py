#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:29:04 2018

@author: hwj
"""

import os
import math
import requests
import numpy as np
import pandas as pd
import time
import datetime
import matplotlib.pyplot as plt

#day_1=pd.read_csv("/hwj/bus/data_transform/20171001/1001_97.csv")
#flag=[0]*len(day_1)
#flag[0]=1
#flag[-1]=1
#for i in range(1,len(day_1)-1):
#    now=day_1.O_NEXTSTATIONNO[i]
#    pre=day_1.O_NEXTSTATIONNO[i-1]
#    pro=day_1.O_NEXTSTATIONNO[i+1]
#    if (now!=pre or now!=pro):
#        flag[i]=1
#day_1.insert(13,'flag',flag)
#day_1=day_1[day_1["flag"]==1]

    
#day_1.to_csv("/hwj/bus/test0.csv")
#datetime.datetime.strptime(day_1.O_TIME.iloc[0],"%H:%M:%S")
#time.strptime(day_1.O_TIME.iloc[0],"%H:%M:%S")
#filelist=os.listdir("/hwj/bus/data_transform/20171001")

#filelist=os.listdir("/hwj/bus/data_transform/20171001")
#for i in filelist:
#    day_1=pd.read_csv("/hwj/bus/data_transform/20171001/"+i)
#    flag=[0]*len(day_1)
#    flag[0]=1
#    flag[-1]=1
#    for j in range(1,len(day_1)-1):
#        now=day_1.O_NEXTSTATIONNO[j]
#        pre=day_1.O_NEXTSTATIONNO[j-1]
#        pro=day_1.O_NEXTSTATIONNO[j+1]
#        if (now!=pre or now!=pro):
#            flag[j]=1
#    day_1.insert(13,"flag",flag)
#    day_1=day_1[day_1["flag"]==1]
#    day=day_1.iloc[:,[1,2,3,10,12]]
#    day.to_csv("/hwj/bus/data_small/"+i,index=0)

out_filelist=os.listdir("/hwj/bus/data_transform")
for m in ['20171001']:
    os.mkdir("/hwj/bus/data_small/"+m+"_small")
    filelist=os.listdir("/hwj/bus/data_transform/"+m)
    for i in filelist:
        day_1=pd.read_csv("/hwj/bus/data_transform/"+m+"/"+i)
        flag=[0]*len(day_1)
        flag[0]=1
        flag[-1]=1
        for j in range(1,len(day_1)-1):
            now=day_1.O_NEXTSTATIONNO[j]
            pre=day_1.O_NEXTSTATIONNO[j-1]
            pro=day_1.O_NEXTSTATIONNO[j+1]
            if (now!=pre or now!=pro):
                flag[j]=1
        day_1.insert(13,"flag",flag)
        day_1=day_1[day_1["flag"]==1]
        day=day_1.iloc[:,[1,2,3,10,12]]
        day.to_csv("/hwj/bus/data_small/"+m+"_small"+"/"+i,index=0)
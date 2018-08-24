#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:36:29 2018

@author: hwj
"""


import os
import math
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#day_1=pd.read_csv("/hwj/bus/dataset/train1-8/train20171001.csv")
#day_2=pd.read_csv("/hwj/bus/dataset/train1-8/train20171002.csv")
#
#lin1=list(set(day_1.O_LINENO))[0]
#day_1_1=day_1[day_1["O_LINENO"]==lin1]
#bus1=list(set(day_1_1.O_TERMINALNO))[0]
#day_1_1_1=day_1_1[day_1_1["O_TERMINALNO"]==bus1]
#day_1_1_1=day_1_1_1.sort_index(axis = 0,ascending = True,by = 'O_TIME')

file="/hwj/bus/dataset/train9-16"
for i in range(8):
    index_str=str(i+9)
    if len(index_str)==1:
        os.mkdir("/hwj/bus/data_transform/2017100"+index_str)
        day=pd.read_csv(file+"/train2017100"+index_str+".csv")
        line_list=list(set(day.O_LINENO))
        for line in line_list:
            day_1=day[day["O_LINENO"]==line]
            day_1=day_1.sort_index(axis = 0,ascending = True,by = ['O_TERMINALNO','O_TIME'])
            day_1.to_csv("/hwj/bus/data_transform/2017100"+index_str+"/100"+index_str+"_"+str(line)+".csv")
    elif len(index_str)==2:
        os.mkdir("/hwj/bus/data_transform/201710"+index_str)
        day=pd.read_csv(file+"/train201710"+index_str+".csv")
        line_list=list(set(day.O_LINENO))
        for line in line_list:
            day_1=day[day["O_LINENO"]==line]
            day_1=day_1.sort_index(axis = 0,ascending = True,by = ['O_TERMINALNO','O_TIME'])
            day_1.to_csv("/hwj/bus/data_transform/201710"+index_str+"/10"+index_str+"_"+str(line)+".csv")
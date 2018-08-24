#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:34:09 2018

@author: hwj
"""

import pandas as pd
import numpy as np

data_median = pd.read_csv("/hwj/bus/predict_table_lll2.csv")
data_mean = pd.read_csv("/hwj/bus/predict_table_lll1.csv")

median = data_median.pred_timeStamps
mean = data_mean.pred_timeStamps

length_median = len(data_median)
length_mean = len(data_mean)

print(length_median, length_mean)

data_median = data_median.rename(index=str, columns={"pred_timeStamps": "median"})
data_mean = data_mean.rename(index=str, columns={"pred_timeStamps": "mean"})

data_total = pd.merge(data_median, data_mean)
data_x = data_total.drop(['median', 'mean'], axis = 1)

timeStamps = []

for i in range(len(data_median)):
    median_list = [int(x) for x in data_total['median'].iloc[i].split(";")]
    mean_list = [int(x) for x in data_total['mean'].iloc[i].split(";")]
    result = [str(int((a+b)/2)) for a,b in zip(median_list,mean_list)]
    timeStamps.append(';'.join(result))
    
pred_timeStamps=pd.DataFrame(timeStamps,columns=["pred_timeStamps"])
predict_table=pd.concat([data_x,pred_timeStamps],axis=1)
predict_table.to_csv("/hwj/bus/train_table_mm.csv",index=0)

df = pd.read_csv("/hwj/bus/train_table_mm.csv")

    
    

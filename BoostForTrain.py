#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 15:48:06 2018

@author: root
"""

import math
import random
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.utils import shuffle
from matplotlib import pyplot as plt

data = pd.read_csv("/root/bus/predict_table_lll2.csv")
#data = data.sample(frac=1).reset_index(drop = True)
#data_y = data.timeStamps
#data_x = data.drop(['timeStamps'], axis = 1)
#X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.33, random_state=42)
#
#train = pd.concat([X_train,y_train], axis=1).reset_index(drop = True)
#test = pd.concat([X_test,y_test], axis=1).reset_index(drop = True)

def transform(data):
    data_transform = pd.DataFrame(columns = ['O_DATA', 'O_LINENO', 'predHour',
                                             'staion', 'median'])
    data_length = len(data)
    for i in range(data_length):
        df_between = {}
        length = len(data.pred_timeStamps.iloc[i].split(";"))
        df_between['O_DATA'] = [int(data.O_DATA.iloc[i].split("-")[1])] * length
        df_between['O_LINENO'] = [data.O_LINENO.iloc[i]] * length
        df_between['predHour'] = [int(data.predHour.iloc[i].split(":")[0])] * length
        df_between['staion'] = list(range(data.pred_start_stop_ID.iloc[i], data.pred_end_stop_ID.iloc[i] + 1))
#        df_between['timeStamps'] = [int(x) for x in data.timeStamps.iloc[i].split(";")]
        df_between['median'] = [int(x) for x in data.pred_timeStamps.iloc[i].split(";")]
        df_todf = pd.DataFrame.from_dict(df_between,orient='index').T
        data_transform = pd.concat([data_transform,df_todf])
        print(i)
    return(data_transform)

def histgram(data,no):
    data_length = len(data)
    list_h = []
    for i in range(data_length):
        time = [int(x) for x in data.predict[i].split(";")]
        if len(time) >= no:
            list_h.append(math.log(time[no-1]))
    plt.hist(list_h,100)
    return(list_h)

test_transform = transform(data)
test_transform.to_csv("/root/bus/test_transform.csv")


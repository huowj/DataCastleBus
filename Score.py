#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 18:10:11 2018

@author: hwj
"""

"""
so this is a test file to calculate the final score
"""

import pandas as pd
import numpy as np

actual_data = pd.read_csv("/hwj/bus/rest_train.csv")
predict_data = pd.read_csv("/hwj/bus/train_table_SameMedian.csv")

actual = actual_data.timeStamps
predict = predict_data.predict

print(len(actual))
print(len(predict))

length_total = len(actual)
rmse_total = 0
rmse_list = []

for i in range(length_total):
    act = np.array([int(x) for x in actual[i].split(";")])
    pre = np.array([int(x) for x in predict[i].split(";")])
    l = len(act)
    rmse = (((act-pre)**2).sum()/length_total) ** (0.5)
    rmse_total += rmse
    rmse_list.append(rmse)

a = rmse_total / (length_total * 100)
print(a)
    
    
    
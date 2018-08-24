#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:14:38 2018

@author: hwj
"""

import numpy as np
import pandas as pd
from catboost import Pool, CatBoostRegressor

# initialize data
train_data = pd.read_csv("/hwj/bus/train_total.csv")
test_data = pd.read_csv("/hwj/bus/test_transform.csv")

X_train = train_data.drop(['timeStamps'], axis = 1)
y_train = train_data.timeStamps


# specify the training parameters 
model = CatBoostRegressor(
        iterations=100,
        depth=4,
        learning_rate=0.5,
        loss_function='RMSE')

#train the model
model.fit(
        X_train, y_train,
        cat_features=np.array([0,1,3,4]),
#        eval_set=(X_validation, y_validation),
        plot=True
        );

# make the prediction using the resulting model
preds = model.predict(test_data)
print(preds)

predict = pd.DataFrame(preds,columns=["predict"])
result_table = pd.concat([test_data,predict], axis = 1)

pred_time = []
a = str(int(result_table.predict[0]))
length = len(result_table)
for i in range(1,length):
    if (result_table.staion[i] == result_table.staion[i-1]+1
        and result_table.O_LINENO[i] == result_table.O_LINENO[i-1]):
        a=a+";"+str(int(result_table.predict[i]))
    else:
        pred_time.append(a)
        a=str(int(result_table.predict[i]))
pred_time.append(a)

testdata0=pd.read_csv("/hwj/bus/dataset/toBePredicted_forUser.csv")
testdata1=testdata0.drop('O_UP',1)

pred_timeStamps=pd.DataFrame(pred_time,columns=["pred_timeStamps"])
predict_table=pd.concat([testdata1,pred_timeStamps],axis=1)
predict_table.to_csv("/hwj/bus/predict_table_catboost0.csv",index=0)

d = pd.read_csv("/hwj/bus/predict_table_lll3.csv")
    
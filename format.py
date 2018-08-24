#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:39:00 2018

@author: hwj
"""


data=pd.read_csv("/hwj/bus/predict_table_lll1.csv")
#data1=data.iloc[:,1:7]
#
#date=data.O_DATA
#
#x=[]
#
#for i in range(len(data)):
#    x.append('10-'+date[i].split("-")[0])
#    
#O_DATA=pd.DataFrame(x,columns=["O_DATA"])
#predict_table=pd.concat([O_DATA,data1],axis=1)

#predict_table.to_csv("/hwj/bus/predict_table_1.csv",index=0)

pred_timeStamps=data.pred_timeStamps
data1=pd.read_csv("/hwj/bus/toBePredicted.csv")
predict_tabl0_1=pd.concat([data1,pred_timeStamps],axis=1)
predict_tabl0_1.to_csv("/hwj/bus/predict_table_lll1.csv",index=0)
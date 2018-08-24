#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 12:17:23 2018

@author: root
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

df1 = pd.DataFrame(columns = ["O_DATA", "O_LINENO", "O_TERMINALNO", "predHour", "pred_start_stop_ID", "pred_end_stop_ID", "O_UP", "pred_timeStamps"])

for day in range(25,32):
    file_name = "/root/bus/data_small/201710" + str(day) + "_small"
    file_list = os.listdir(file_name)
    for file in file_list:
        data_name = "/root/bus/data_small/201710" + str(day) + "_small/" + file
        data = pd.read_csv(data_name)
        data['hour'] = data.O_TIME.map(lambda x:int(str(x)[0:2]))
        bus_list = list(set(data.O_TERMINALNO))
        for bus in bus_list:
            data_bus = data[data['O_TERMINALNO'] == bus]
            bus_hour_list = list(set(data_bus.hour))
            for hour in bus_hour_list:
                data_bus_hour = data_bus[data_bus['hour'] == hour]
                first_hour = data_bus_hour.O_TIME.iloc[0][0:2]
                first_minute = int(data_bus_hour.O_TIME.iloc[0][3:5])
                first_second = int(data_bus_hour.O_TIME.iloc[0][6:8])
                first_up = data_bus_hour.O_UP.iloc[0]
                start_station = data_bus_hour.O_NEXTSTATIONNO.iloc[0]
                end_station = start_station + 1
#                print(end_station)
                length = len(data_bus_hour)
                time_stamp = []
                station_stamp = []
                if (first_minute == 0 and first_second < 11):
                    for i in range(1,length):
                        now_station = data_bus_hour.O_NEXTSTATIONNO.iloc[i]
                        now_up = data_bus_hour.O_UP.iloc[i]
                        if (now_up == first_up and now_station == end_station):
                            interval_time = int(data_bus_hour.O_TIME.iloc[i][3:5])*60 + int(data_bus_hour.O_TIME.iloc[i][6:8])
#                            print(time)
                            time_stamp.append(interval_time)
                            station_stamp.append(now_station - 1)
                            end_station+=1
                if (len(time_stamp) > 5):
                    df_list = {}
                    df_list["O_DATA"] = '10-'+str(day)
                    df_list["O_LINENO"] = file.split("_")[1][:-4]
                    df_list["O_TERMINALNO"] = bus
                    df_list["predHour"] = first_hour + ":00:00"
                    df_list["pred_start_stop_ID"] = start_station
                    df_list["pred_end_stop_ID"] = station_stamp[-1]
                    df_list["O_UP"] = first_up
                    time_stamp_str = [str(j) for j in time_stamp]
                    df_list["pred_timeStamps"] = ';'.join(time_stamp_str)
                    df_list_todf = pd.DataFrame.from_dict(df_list,orient='index').T
                    df1 = pd.concat([df1,df_list_todf])

df1.to_csv("/root/bus/rest_train.csv", index = 0)
                    
                    
                    
                    
                        
                            
                        
                    
                
                
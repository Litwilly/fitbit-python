#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# https://dev.fitbit.com/docs

import requests
import json
import time
import datetime
import os

filename = "{path to]/refresh.py"
execfile(filename)

def get_sleep(datevar):
    # date should be a datetime.date object ie "2016-03-23".
    url = "https://api.fitbit.com/1/user/-/sleep/date/"+datevar+".json"
    access_path = "{path declared in refresh.py}/access.txt"

    # open and read refresh.txt to var remove newline
    opr = open(access_path, "r")
    token = opr.readline().strip()
    access_token = "Bearer %s" % (token) 
    opr.close()

    headers = {
        'authorization': access_token,
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers)
    #print(response.text)
    return response.json()

#get todays date
to = time.strftime("%Y-%m-%d")

#run funtion with todays date
get_sleep(to)

#if there is sleep data print specific json elements
if len(todayvar['sleep']) >= 1:
    myvar = todayvar['sleep'][0]['isMainSleep']
    startTime = todayvar['sleep'][0]['startTime']
    print(myvar)
    print(startTime)
else:
    print("No Sleep Data")

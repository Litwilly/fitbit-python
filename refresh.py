#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests

url = "https://api.fitbit.com/oauth2/token"
refresh_path = "{path to refresh token}/refresh.txt"
access_path = "{path to access token}/access.txt"

# open and read refresh.txt to var remove newline
opr = open(refresh_path, "r")
refresh_token = opr.readline().strip()
opr.close()

# contruct headers
querystring = {"grant_type":"refresh_token","refresh_token":refresh_token}
headers = {
    'authorization': "Basic {your authorization string here}",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

# POST our refresh token request
response = requests.request("POST", url, headers=headers, params=querystring)

# save in JSON
json = response.json()

# store our tokens
newrefresh = json['refresh_token']
access_token = json['access_token']

# open, wipe, write new refresh token to refresh.txt
opw = open(refresh_path, "w")
opw.truncate
opw.write(newrefresh)
opw.close()

# open, wipe, write new access token to access.txt
opaw = open(access_path, "w")
opaw.truncate
opaw.write(access_token)
opaw.close()


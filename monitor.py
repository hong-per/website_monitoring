#!/bin/bash

# Importing libraries
import requests
import time
import hashlib
from urllib.request import urlopen, Request

# setting Chatwork Token and ROOMID
Token = ''
ROOMID = ''
api_url = 'https://api.chatwork.com/v2'

# setting the URL you want to monitor
target = ''

url = Request(target, 
              headers={'User-Agent': 'Mozilla/5.0'})

# setting ChatWork Message
message = f"""
"""


while True:
    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()
          
        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()
          
        # wait for 300 seconds
        time.sleep(300)
          
        # perform the get request
        response = urlopen(url).read()
          
        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()
  
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue
  
        # if something changed in the hashes
        else:
            # notify
            # print("something changed")
            chat_url = api_url + '/rooms/' + ROOMID + '/messages'
            headers = { 'X-ChatWorkToken': Token }
            params = { 'body': message }

            resp = requests.post(chat_url,
                                 headers=headers,
                                 params=params)
  
            # again read the website
            response = urlopen(url).read()
  
            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()
  
            # wait for 300 seconds
            time.sleep(300)
            continue
              
    # To handle exceptions
    except Exception as e:
        print("error")
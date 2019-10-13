# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:45:33 2019

@author: srishti
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:07:14 2019

@author: srishti
"""

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

import time
import json
phrase_to_search = 'Modi'

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

g=[]
class StdOutListener(StreamListener):
    def on_data(self,data):
        global g
        y=json.loads(data)
        print(y["text"])
        g.append(y["text"])
        #print(g)
        #time.sleep(2) 
        return True

    # To print the status if an error happens
    def on_error(self,status):
        print(status)


def cal_api(phrase):
    global g

    # If the time crosses the amount of time mentioned by t_end, then the tweet scrapping stops
    try:
        cont.filter(track=[phrase])
    except Exception as e:
        print(e)

    # If the stream is already connected, the following will disconnect the stream and reconnect it
    if "Stream object already connected!"==(str(e)):
        cont.disconnect()
        print("connecting again")
        cont.filter(track=[phrase])



if __name__=='__main__':
    listen = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    cont=Stream(auth,listen)
    
cal_api(phrase_to_search)



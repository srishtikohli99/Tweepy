# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:40:14 2019

@author: srishti
"""

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import re

import time
import json
phrase_to_search = '#Charminar'

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


authorizer = OAuthHandler(consumer_key, consumer_secret)
authorizer.set_access_token(access_token, access_secret)


api = tweepy.API(authorizer ,timeout=15)

all_tweets = []

search_query = 'microsoft'

for tweet_object in tweepy.Cursor(api.search,q=search_query+" -filter:retweets",lang='en',result_type='recent').items(200):
    all_tweets.append(tweet_object.text)


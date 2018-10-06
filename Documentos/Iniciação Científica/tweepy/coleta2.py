#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import csv
import sys


API_KEY = 'C6JpFOm1Iyy7j0L4J2mCWCXH2'
API_SECRET = 'mJeVHVQcQLZIehtxlUeWaNxGhuwqXzTsnQ8arv6SnFdi0NN6ZR'
ACCESS_TOKEN = '986415660-edDXhBSJvdBlUgwmJFZTUa7zNK3qhhaGKBa1Rhkh'
ACCESS_TOKEN_SECRET = 'eaBrLDVfAbbxZHRu0GXKQPruDzCzrgBbxl6FvLfMnfYZV'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

csvFile = open('debateGlobo.csv', 'a')
csvWriter = csv.writer(csvFile)


query = '#bolsonaro'
max_tweets = 20000

searched_tweets = []
last_id = -1
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
    try:
        new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1), tweet_mode='extended')
        if not new_tweets:
            break
        searched_tweets.append(new_tweets)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        break

#print searched_tweets[0]

for tweet in searched_tweets:
	print tweet
	print
	print
    #csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8')])

csvFile.close()

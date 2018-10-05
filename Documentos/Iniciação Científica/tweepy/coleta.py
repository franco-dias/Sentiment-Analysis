import tweepy
import csv

API_KEY = 'C6JpFOm1Iyy7j0L4J2mCWCXH2'
API_SECRET = 'mJeVHVQcQLZIehtxlUeWaNxGhuwqXzTsnQ8arv6SnFdi0NN6ZR'
ACCESS_TOKEN = '986415660-edDXhBSJvdBlUgwmJFZTUa7zNK3qhhaGKBa1Rhkh'
ACCESS_TOKEN_SECRET = 'eaBrLDVfAbbxZHRu0GXKQPruDzCzrgBbxl6FvLfMnfYZV'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

csvFile = open('debateBand.csv', 'a')
csvWriter = csv.writer(csvFile)

query = '#DebateBand'
max_tweets = 1000
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

for tweet in searched_tweets:
	    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

csvFile.close()

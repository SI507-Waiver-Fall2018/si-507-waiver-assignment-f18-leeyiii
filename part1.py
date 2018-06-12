# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
# usage should be python3 part1.py <username> <num_tweets>

consumer_key="Fe8SgOwx3kLZdKBkheaXsUI17"
consumer_secret="Ypl7Tlf3HJHvaipbJE7oyB8afG0WIixXRVxDqviMXvVwUqns4Z"
access_token="4858990592-0HfFBiXrZZtUg6AWLvVOcrprkUIErJ4F28rAnIL"
access_token_secret="Bik4x8ctRYvY5rGgSTeGYbVyc7IHs9OQ5CKiHjsOpKTvs"

auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#test

public_tweets = api.home_timeline()

for tweet in public_tweets:
	print (tweet.text)
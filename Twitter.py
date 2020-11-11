import tweepy
import time
import os
from os import environ

api_key= environ['api_key']
api_secret= environ['api_secret']
access_token= environ['access_token']
secret_token= environ['secret_token']

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, secret_token)

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user=api.me()


search = 'careca'
numeroDeTweets = 2000

for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
    try:
        print('tweet Retuitado e favoritado')
        tweet.retweet()
        tweet.favorite()
        time.sleep(15)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
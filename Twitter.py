import tweepy
import time
import tokens

auth = tweepy.OAuthHandler(tokens.api_key,tokens.api_secret)
auth.set_access_token(tokens.access_token,tokens.secret_token)

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
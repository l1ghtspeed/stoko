import os
import tweepy
from stream import StreamListener

API_KEY, API_SECRET = os.environ['twitter_api_key'], os.environ['twitter_api_secret']
ACCESS_TOKEN, ACCESS_SECRET = os.environ['twitter_access_token'], os.environ['twitter_access_secret']
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

stream_listener = StreamListener()
stream = tweepy.Stream(auth = api.auth, listener=stream_listener)
stream.filter(track=['bitcoin'])

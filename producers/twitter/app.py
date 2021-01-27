import os
import tweepy
from json import dumps
from kafka import KafkaProducer
from stream import StreamListener


ACCESS_TOKEN, ACCESS_SECRET = os.environ['twitter_access_token'], os.environ['twitter_access_secret']
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


producer = KafkaProducer(
            bootstrap_servers=[os.environ['kafka_bootstrap_server']],
            value_serializer=lambda x: dumps(x).encode('utf-8')
          )

stream_listener = StreamListener(producer)
stream = tweepy.Stream(auth = api.auth, listener=stream_listener)
stream.filter(track=['bitcoin'])

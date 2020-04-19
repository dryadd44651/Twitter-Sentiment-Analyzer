from kafka import KafkaProducer
import kafka
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# TWITTER API CONFIGURATIONS
consumer_key = "je8lIMRYPX0YGpKSZy9NqBkHH"
consumer_secret = "PBv6cDYVCWG2qTA22Gff5EHHyBajuIiONHF1GR5qjatgDOKYRl"
access_token = "1248098817037045760-sIXPEkAFu8H7Q0qKiK4uhmWDp8eect"
access_secret = "Zt7Hs0IWkpCwGEiWnYmcBIZZlIMU3VfPdbx9LsDdFl8Ro"

# TWITTER API AUTH
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# Twitter Stream Listener
class KafkaPushListener(StreamListener):
    def __init__(self):
        # localhost:9092 = Default Zookeeper Producer Host and Port Adresses
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    # Get Producer that has topic name is Twitter
    # self.producer = self.client.topics[bytes("twitter")].get_producer()

    def on_data(self, data):
        # Producer produces data for consumer
        # Data comes from Twitter
        self.producer.send("twitter", data.encode('utf-8'))
        print(data)
        return True

    def on_error(self, status):
        print(status)
        return True


# Twitter Stream Config
twitter_stream = Stream(auth, KafkaPushListener())

# Produce Data that has trump hashtag (Tweets)
twitter_stream.filter(track=['#trump'])#'#trump','#coronavirus']
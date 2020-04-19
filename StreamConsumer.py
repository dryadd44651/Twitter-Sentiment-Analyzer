from kafka import KafkaConsumer
import json
from elasticsearch import Elasticsearch
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
es = Elasticsearch()

def classify(sentence):
	sid_obj = SentimentIntensityAnalyzer()
	sentiment_dict = sid_obj.polarity_scores(sentence)
	if sentiment_dict['compound'] >= 0.05:
		return "Positive"
	elif sentiment_dict['compound'] <= - 0.05 :
		return "Negative"
	else:
		return "Neutral"

def main():

	consumer = KafkaConsumer("twitter")
	for msg in consumer:
		try:
			dict_data = json.loads(msg.value)
			tweet = TextBlob(dict_data["text"])
			print(tweet)
			# add text and sentiment info to elasticsearch

			es.index(index="tweet",
					doc_type="test-type",
					body={"author": dict_data["user"]["screen_name"],
						"date": dict_data["created_at"],
						"message": dict_data["text"],
						"sentiment": classify(dict_data["text"])
						})

			print('\n')
		except:
			print('error')
if __name__ == "__main__":
    main()
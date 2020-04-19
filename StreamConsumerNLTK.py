from kafka import KafkaConsumer
import json
from elasticsearch import Elasticsearch
from textblob import TextBlob
import nltkModel

def classify(prob,range):
    nprob = pow(10,prob['Negative'])
    pprob = pow(10,prob['Positive'])
    diff = pprob - nprob
    if (nprob < range and  pprob < range) or abs(diff) < range:
        return 'Neutral'
    elif diff>0:
        return 'Positive'
    else:
        return 'Negative'


def main():
    es = Elasticsearch()
    classifier =  nltkModel.get_model()
    consumer = KafkaConsumer("twitter")
    for msg in consumer:
        try:
            dict_data = json.loads(msg.value)
            test = nltkModel.get_test_dict(dict_data["text"])
            prob = classifier.prob_classify(test)._prob_dict
            sentiment = classify(prob,0.1)
            tweet = TextBlob(dict_data["text"])
            #print(tweet)
            print(dict_data["created_at"], dict_data["user"]["screen_name"], dict_data["text"])
            #print(dict_data["entities"]["hashtags"])
            # add text and sentiment info to elasticsearch

            es.index(index="tweet_trump",
                    doc_type="test-type",
                    body={"author": dict_data["user"]["screen_name"],
                        "date": dict_data["created_at"],
                        "message": dict_data["text"],
                        "sentiment": sentiment
                        })

            print('\n')
        except:
            print('error')
if __name__ == "__main__":
    main()
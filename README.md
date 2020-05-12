# Twitter-Sentiment-Analyzer
The project implemented the following framework using Apache Spark Streaming, Kafka (optional), Elastic, and Kibana.

The project performs SENTIMENT analysis of particular hash tags in twitter data in real-time.

1. Scrapper
Collecting tweets in real-time with particular hash tags. For example, we
will collect all tweets with #trump, #coronavirus. After filtering, we will send them to Kafka

2. Kafka 
install Kafka and run Kafka Server with Zookeeper. create a dedicated channel/topic for data transport.
3. Spark Streaming
In Spark Streaming, create a Kafka consumer from scrapper. For each hash tag, perform sentiment analysis
using Sentiment Analyzing tool(NLTK).

4. Natural Language Toolkit
In nltkModel.py, We get the training twitter sample from NLTK.

We ETL the data
- Tokenizing and Stemming 
- (removing all irrelevant characters such as any non alphanumeric characters.)
- lemmatizing the data.
- lengthening(gooood = > good) and Spell Check(Time-consuming)
Train the data with NaiveBayesClassifier

5. Elasticsearch
install the Elasticsearch and run it to store the tweets and their sentiment information for further visualization purpose.

6. Kibana
Kibana is a visualization tool that can explore the data stored in elasticsearch.


run cmd.bat
- start the zookeeper-server, kafka-server, elasticsearch, kibana
- create the kafka-topics
- elasticsearch: http://localhost:200
- kibana: http://localhost:5601/

python StreamProducer.py

python StreamConsumer.py  or  StreamConsumerNLTK.py

StreamConsumerNLTK uses NLTK with nltkModel.py

StreamConsumer uses VADER

more sample code please check VADER.py, nlp_test.py, nltk.ipynb, nltkModel.py

nltk.ipynb: nltk traing, Word2Vec word embeddings, sklearn machine learning model

![tweet_dashboard.JPG](https://github.com/dryadd44651/Twitter-Sentiment-Analyzer/blob/master/tweet_dashboard.JPG)



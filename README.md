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
We clean the data
- removing all irrelevant characters such as any non alphanumeric characters.
- lemmatize the data.
- lengthening and Spell Check(Time-consuming)
Train the data with NaiveBayesClassifier

5. Elasticsearch
install the Elasticsearch and run it to store the tweets and their sentiment information for further visualization purpose.

6. Kibana
Kibana is a visualization tool that can explore the data stored in elasticsearch.

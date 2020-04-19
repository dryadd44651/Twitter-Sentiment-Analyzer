from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier,ConditionalExponentialClassifier,DecisionTreeClassifier,MaxentClassifier
import re, string, random
import pickle
import os.path
from os import path


def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)


def get_tweets_dataset():
    positive_tweets = twitter_samples.strings('positive_tweets.json')
    negative_tweets = twitter_samples.strings('negative_tweets.json')
#     text = twitter_samples.strings('tweets.20150430-223406.json')
#     tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]

    stop_words = stopwords.words('english')

    positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []

    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

#     all_pos_words = get_all_words(positive_cleaned_tokens_list)

#     freq_dist_pos = FreqDist(all_pos_words)
#     print(freq_dist_pos.most_common(10))

    positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)

    positive_dataset = [(tweet_dict, "Positive")
                         for tweet_dict in positive_tokens_for_model]

    negative_dataset = [(tweet_dict, "Negative")
                         for tweet_dict in negative_tokens_for_model]

    dataset = positive_dataset + negative_dataset

    random.shuffle(dataset)

    return dataset

def get_model(modelName = 'NaiveBayesClassifier'):
#     ConditionalExponentialClassifier
#     DecisionTreeClassifier
#     MaxentClassifier
#     NaiveBayesClassifier
    if modelName == 'NaiveBayesClassifier':
        model = NaiveBayesClassifier
    elif modelName == 'MaxentClassifier':
        model = MaxentClassifier
    elif modelName == 'DecisionTreeClassifier':
        model = DecisionTreeClassifier
    elif modelName == 'ConditionalExponentialClassifier':
        model = ConditionalExponentialClassifier

    modelName = modelName+'.pickle'
    if path.exists(modelName):
        f = open(modelName, 'rb')
        classifier = pickle.load(f)
        f.close()
    else:
        dataset = get_tweets_dataset()
        train_data = dataset[:7000]
        test_data = dataset[7000:]
        classifier = model.train(train_data)
        #print(classifier.show_most_informative_features(10))
        f = open(modelName, 'wb')
        pickle.dump(classifier, f)
        f.close()
        print("Accuracy is:", classify.accuracy(classifier, test_data))

    return classifier

def get_test_dict(custom_tweet):
    custom_tokens = remove_noise(word_tokenize(custom_tweet))
    return dict([token, True] for token in custom_tokens)
# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # oject gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

    print("Sentence Overall Rated As", end = " ")
    print("sentiment_dict['compound'] ",sentiment_dict['compound'])
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")

    else :
        print("Neutral")
    return "Positive"



# Driver code
if __name__ == "__main__" :

    print("\n1st statement :")
    sentence = "President Donald Trump approaches his first big test this week from a\
position of unusual weakness."

    # function calling
    sentiment_scores(sentence)

    print("\n2nd Statement :")
    sentence = "Trump has the lowest standing in public opinion of any new president in\
modern history."

    sentiment_scores(sentence)

    print("\n3rd Statement :")
    sentence = "Trump has displayed little interest in the policy itself, casting it as a\
thankless chore to be done before getting to tax-cut legislation he values more."
    sentiment_scores(sentence)
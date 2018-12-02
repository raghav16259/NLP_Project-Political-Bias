from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
text = '''
Modi govt faces flak for new BPL criteria.
'''

blob = TextBlob(text)
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)


# -0.7
# 0.0
# 0.5



analyser = SentimentIntensityAnalyzer()

def print_sentiment_scores(tweets):
    vadersenti = analyser.polarity_scores(tweets)
    print(vadersenti['compound'])
    #return pd.Series([vadersenti['pos'], vadersenti['neg'], vadersenti['neu'], vadersenti['compound']])

text = 'That situation was good best awesome.'
print_sentiment_scores(text)

"""The results are:
0    0.2470
1    0.0000
2    0.7530
3    0.5067"""
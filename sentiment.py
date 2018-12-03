import sys
sys.path.append('c:\python34\lib\site-packages')
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pickle
def blobscore(text):
    blob = TextBlob(text)
    ret = 0
    for sentence in blob.sentences:
        ret = (sentence.sentiment.polarity)
    return ret
def print_sentiment_scores(text):
    analyser = SentimentIntensityAnalyzer()
    vadersenti = analyser.polarity_scores(text)
    return(vadersenti['compound'])
    #return pd.Series([vadersenti['pos'], vadersenti['neg'], vadersenti['neu'], vadersenti['compound']])
def divide():
    file = open("filter_headlines_2014.pkl",'rb')
    source_headlines = pickle.load(file)
    predicted =[{},{},{}]
    actual = [{},{},{}]
    m =0
    for j in range(len(source_headlines)):
        for k in source_headlines[j]:
            for i in source_headlines[j].get(k):
                score1 = blobscore(i)
                score2 = print_sentiment_scores(i)
                avg = 0.7*(score2)+0.3*(score1)
                predicted[j][k] = [i,avg]
                actual[j][k] =[i,score2]
                print(m)
                m+=1
    file2 = open("predicted.pkl",'wb')
    pickle.dump(predicted,file2)
    file2 = open("actual.pkl",'wb')
    pickle.dump(actual,file2)
divide()

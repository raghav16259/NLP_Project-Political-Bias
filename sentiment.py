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
pkl_file = open('pickle2.pkl', 'rb')
headlines = pickle.load(pkl_file)
picklefinal =[]
j=0
def divide():
    file = open("source_headlines.pkl",'rb')
    source_headlines = pickle.load(file)
    cong = ['cong','congress','gandhi','sonia','inc','rahul']
    bjp =['bjp','modi','narendra','amit']
    aap =['aap','sisodia','kejriwal']
    divide =[]
    source_party=[]
    for j in source_headlines:
        cong1=[]
        bjp1=[]
        aap1=[]
        for i in source_headlines.get(j):
            cong2 =0
            bjp2 =0
            aap2 =0
            l = i.split()
            for j in l:
                if j.lower()in cong:
                    cong2 =1   
                if j.lower()in bjp:
                    bjp2 = 1
                if j.lower()in aap:
                    aap2 = 1
            if(cong2==1 and(bjp2!=1 and aap2!=1)):
                score1 = blobscore(i)
                score2 = print_sentiment_scores(i)
                avg = (score1+score2)/2
                cong1.append(i+";"+str(avg))
            if(bjp2==1 and(cong2!=1 and aap2!=1)):
                score1 = blobscore(i)
                score2 = print_sentiment_scores(i)
                avg = (score1+score2)/2
                bjp1.append(i+";"+str(avg))
            if(aap2==1 and(cong2!=1 and bjp2!=1)):
                score1 = blobscore(i)
                score2 = print_sentiment_scores(i)
                avg = (score1+score2)/2
                cong1.append(i+";"+str(avg))
                
        l =[]
        l.append(cong1)
        l.append(bjp1)
        l.append(aap1)
        source_party.append([j,l])
    file2 = open("source_party.pkl",'wb')
    pickle.dump(source_party,file2)
divide()
for i in headlines:
    score1 = blobscore(i[0])
    score2 = print_sentiment_scores(i[0])
    print(score1)
    print(score2)
    avg = (score1+score2)/2
    
file2 = open("sentiment.pkl",'wb')
pickle.dump(picklefinal,file2)
file.close()
"""The results are:
0    0.2470
1    0.0000
2    0.7530
3    0.5067"""

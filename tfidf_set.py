import pickle as pkl
import math
'''
pkl_file = open('pickle2.pkl', 'rb')
headlines = pkl.load(pkl_file)
source_headlines={}
j=0
for i in headlines:
    key = i[1]
    if(source_headlines.get(key)!=None):
        l = source_headlines.get(key)
        l.append(i[0])
        source_headlines[i[1]] = l
    else:
        l =[]
        l.append(i[0])
        source_headlines[key] = l 
file2 = open("source_headlines.pkl",'wb')
pkl.dump(source_headlines,file2)
'''
file = open("source_headlines.pkl",'rb')
count = {'bjp':0,'cong':0,'congress':0,'rahul':0,'gandhi':0,'sonia':0,'inc':0,'narendra':0,'modi':0,'amit':0,'kejriwal':0,'aap':0,'sisodia':0}
words = {}
tf=[]
source_headlines= pkl.load(file)
for j in source_headlines:
    total =0
    for i in source_headlines.get(j):
        for k in i.split():
            if(count.get(k.lower())!=None):
                c = count.get(k.lower())
                c = c+1
                count[k.lower()] = c
            if(words.get(k.lower())==None):
                total+=1
                words[k.lower()] = 1
    tf.append([j,[count.get('bjp'),count.get('cong'),count.get('congress'),count.get('rahul'),count.get('gandhi'),count.get('sonia'),count.get('inc'),count.get('narendra'),count.get('modi'),count.get('amit'),count.get('kejriwal'),count.get('aap'),count.get('sisodia')]])
    count = {'bjp':0,'cong':0,'congress':0,'rahul':0,'gandhi':0,'sonia':0,'inc':0,'narendra':0,'modi':0,'amit':0,'kejriwal':0,'aap':0,'sisodia':0}
    words={}
#print(tf)
#print (len(tf))
df =[0]*len(count)
for j in tf:
    for i in range(0,len(count)):
        if(j[1][i]>0):
            df[i]+=1

#print(df)
idf = [0]*len(count)
for j in range(len(df)):
    idf[j] = math.log10(len(tf)/(df[j]+1))
        
#print(idf)
w =[]
for i in range(0,len(count)):
    w.append([])
    for j in range(len(tf)):
        w[i].append(float(tf[j][1][i])*idf[i])
print(w)        

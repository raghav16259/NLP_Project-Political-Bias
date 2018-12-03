import pickle
fname="/Users/raghav/Desktop/Courses/Natural Language Processing/Political Bias/Megatable-2014.txt"
with open(fname) as f:
    text=f.readlines()
#print(text)

headlines=[]

for i in range(len(text)):
    splitted=text[i].split(",")
    news=splitted[1][2:-1]
    source=splitted[-2][1:-1]
    l=[]
    l.append(news)
    l.append(source)
    headlines.append(l)
output = open('pickle2.pkl','wb')
pickle.dump(headlines, output)


#print(headlines)

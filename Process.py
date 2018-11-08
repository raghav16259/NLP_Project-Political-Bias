import pickle
pkl_file = open('pickle2.pkl', 'rb')
headlines = pickle.load(pkl_file)
#print(headlines)

fname="/Users/raghav/Desktop/Courses/Natural Language Processing/Political Bias/source.txt"
with open(fname) as f:
    text=f.readlines()
source_dict={}
for i in range(len(text)):
    splitted = text[i].split(",")
    title=splitted[2][2:-1]
    if(title != "sport" and title != "business" and title != "technology" and title != "entertainment" and title!="commentry" and title!= "multimedia" ):
        source_num=splitted[0][1:]
        source_name=splitted[1][2:-1]
        source_dict[source_num]=source_name
print(source_dict)

headlines2=[]
for i in range(len(headlines)):
    if (headlines[i][1] in source_dict):
        headlines2.append(headlines[i])

output = open('pickle2.pkl','wb')
pickle.dump(headlines2, output)

import pickle

pkl_file = open('/Users/raghav/Desktop/Courses/Natural Language Processing/Political Bias/venv/pickle2.pkl', 'rb')
headlines = pickle.load(pkl_file)
file=open("output.txt","w")
for i in headlines:
    file.write(" ".join(str(x) for x in i))
    file.write("\n")
file.close()

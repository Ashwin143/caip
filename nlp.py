from textblob import TextBlob,Word
import nltk,random

#1.1
a=TextBlob("this is good this is bad this can be good  this can be very bad")
b=a.sentences
print(a.sentences)

#1.2

print(a.words)

#1.3

b = TextBlob("ashwin is a great data scientist.")
for t in b.noun_phrases:
    print (t)

#1.4

b = TextBlob(" gret data scintist.")
for t in b.correct():
    print (t)


#1.5

b = TextBlob("good morning")
t=b.translate(from_lang='en', to ='es')
print(t)

#2.1

b = TextBlob("ballon")
t=b.words.pluralize()
print(t)

c = TextBlob("ballons")
t=c.words.singularize()
print(t)

#2.2

b = TextBlob("arun has big ballon")
for tag in b.tags:
    print(tag)

#3

b = TextBlob("iam happy")
t=b.sentiment
print(t)

#4

b = TextBlob("arun has big ballon,each ballon is different,he also likes color ballons")
a=list()
for word,tag in b.tags:
    if tag == 'NN':
        a.append(word.lemmatize())

print ("summary will be as below.....")
for item in random.sample(a, 4):
    word = Word(item)
print (word.pluralize())



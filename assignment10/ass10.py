#1
import tweepy
import re

consumer_key = "4fAlDZOUqbK3xl6dJyzHuoIBt"
consumer_secret = "M13v2MC66SQLbB2VF7FKdi67iGmecTcTdKDnIpUA1yzh5OqyQi" 
access_token = "709977607496933376-UY1nbgAPQU3YyPs2ZSaMhDo5XtNYgaO"
access_token_secret = "pEXLccvY7lvK9pj5ZX4hjAxJW0OgTxrUaYoQ1Pcv82Y1G"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

public_tweets = api.user_timeline(screen_name='@ndtv',count=25) 
tweets_for= [tweet.text for tweet in public_tweets] 

list=[]
for j in tweets_for:
    a=(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",j).split()))
    list.append(a)
# print(list) 
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(documents)


kmeans = KMeans(n_clusters=2)
kmeans.fit(matrix)
labels = kmeans.labels_

for i in range(len(labels)):
	print(str(list[i]) + " belongs to Cluster  " + str(labels[i]) )
#2
import tweepy
import re

consumer_key = "4fAlDZOUqbK3xl6dJyzHuoIBt"
consumer_secret = "M13v2MC66SQLbB2VF7FKdi67iGmecTcTdKDnIpUA1yzh5OqyQi" 
access_token = "709977607496933376-UY1nbgAPQU3YyPs2ZSaMhDo5XtNYgaO"
access_token_secret = "pEXLccvY7lvK9pj5ZX4hjAxJW0OgTxrUaYoQ1Pcv82Y1G"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

public_tweets = api.user_timeline(screen_name='@ndtv',count=5) 
tweets_for= [tweet.text for tweet in public_tweets] 
# for tweet in public_tweets:
#     print(tweet.text)
list=[]
for j in tweets_for:
    a=(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",j).split()))
    list.append(a)
# print(list) 
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(documents)


kmeans = KMeans(n_clusters=2)
kmeans.fit(matrix)
labels = kmeans.labels_

for i in range(len(labels)):
	print(str(list[i]) + " belongs to Cluster  " + str(labels[i]) )

#3







#4

import tweepy
import re

consumer_key = "4fAlDZOUqbK3xl6dJyzHuoIBt"
consumer_secret = "M13v2MC66SQLbB2VF7FKdi67iGmecTcTdKDnIpUA1yzh5OqyQi" 
access_token = "709977607496933376-UY1nbgAPQU3YyPs2ZSaMhDo5XtNYgaO"
access_token_secret = "pEXLccvY7lvK9pj5ZX4hjAxJW0OgTxrUaYoQ1Pcv82Y1G"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

number_of_tweets=20
public_tweets = api.user_timeline(screen_name='@ndtv',count=25) 
tweets_for= [tweet.text for tweet in public_tweets] 
# for tweet in public_tweets:
#     print(tweet.text)
list=[]
for j in tweets_for:
    a=(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",j).split()))
    list.append(a)
# print(list) 
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(list)

r=[]
for i in list:
     b = TextBlob(i)
     t=b.sentiment.polarity
     r.append(t)
print(r)

import pandas as pd        
import matplotlib.pyplot as plot
dataFrame = pd.DataFrame(r)
dataFrame
dataFrame.plot.bar()
plot.xlabel("no of entries")
plot.ylabel("polarity")
plot.show()
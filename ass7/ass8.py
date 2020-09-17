#1

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
import csv
import os
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
X,y_terms=make_blobs(n_samples=500,centers=5,cluster_std=0.6)
plt.scatter(X[:,0],X[:,1],s=50)
plt.show
kmeans=KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)
plt.scatter(X[:,0],X[:,1],s=50,cmap='viridis',c=y_kmeans)
y_kmeans

#2

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
import csv
import os
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix 
df = pd.read_csv(r"D:\\ML\\CAIP\\ass7\\Iris.csv")
df.head(10)

fig=df[df.Species=='Iris-setosa'].plot.scatter(x='SepalLengthCm',y='SepalWidthCm',color='orange', label='Setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SepalLengthCm',y='SepalWidthCm',color='blue', label='versicolor',ax=fig)
df[df.Species=='Iris-virginica'].plot.scatter(x='SepalLengthCm',y='SepalWidthCm',color='green', label='virginica', ax=fig)
fig.set_xlabel("Sepal Length")
fig.set_ylabel("Sepal Width")
fig.set_title(" Sepal Length VS Width")
fig=plt.gcf()
fig.set_size_inches(10,6)
plt.show()
#training the whole dataset 
train_X = train[['SepalLengthCm','SepalWidthCm']]
train_y=train.Species
# output of training dataset
train_y.head(10)
train, test = train_test_split(df, test_size = 0.3)
train_X = train[['SepalLengthCm','SepalWidthCm']]
train_y=train.Species
test_X= test[['SepalLengthCm','SepalWidthCm']] 
test_y =test.Species

model=KNeighborsClassifier(n_neighbors=3) 
model.fit(train_X,train_y)
prediction=model.predict(test_X)
print(metrics.accuracy_score(prediction,test_y))

#3

dataset link  -  http://cs.joensuu.fi/sipu/datasets/Aggregation.txt

data=pd.read_csv('D:/w.csv',header=None,names=["A", "B", "C"])
data.head()
f1=data['A'].values
f2=data['B'].values

X=np.array(list(zip(f1,f2)))

kmeans=KMeans(n_clusters=3)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)


plt.scatter(f1,f2,c=y_kmeans,s=20,cmap='viridis')

centers=kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c="blue",s=200)
plt.show()

#4
data = pd.read_csv(r"D:\ML\CAIP\Assignment8\\Advertising.csv")
data.head()
t=data.drop(data.columns[0], axis=1)
t
plt.figure(figsize=(7,4)) 
sns.heatmap(t.corr(),annot=True,cmap='cubehelix_r')
plt.show()
plt.scatter(data['TV'], data['sales'], color='blue')
plt.xlabel('TV')
plt.ylabel('sales')

X = data['TV'].values.reshape(-1,1)
Y = data['sales'].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
Model = LinearRegression()
Model.fit(X_train, y_train)

train_fit = Model.predict(X_train)
test_pred = Model.predict(X_test)

plt.scatter(X_train, y_train, color='gray')
plt.plot(X_train, train_fit, color='blue', linewidth=2)
plt.xlabel('TV')
plt.ylabel('sales')

plt.scatter(X_test, y_test, color='gray')
plt.plot(X_test, test_pred, color='blue', linewidth=2)
plt.xlabel('TV')
plt.ylabel('sales')

print('Mean Squared Error:', metrics.mean_squared_error(y_test, test_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, test_pred)))
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, test_pred))
print('R2SCORE:', metrics.r2_score(y_test, test_pred))

#5

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
import csv
import os
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

data = pd.read_csv(r"D:\ML\CAIP\Assignment8\\bikeshare\\bike_sharing_hourly.csv")
data.head()
r=data.drop(data.columns[2],axis=1)
r
plt.figure(figsize=(20,10)) 
sns.heatmap(r.corr(),annot=True,cmap='cubehelix_r')
plt.show()
cols = ['casual', 'registered','cnt']
list = r[cols]
r.set_index('dteday', inplace = True)
list.head(10)

plt.figure(figsize=(10,5)) 
sns.heatmap(list.corr(),annot=True,cmap='cubehelix_r')
plt.show()

plt.scatter(data['casual'], data['cnt'], color='blue')
plt.xlabel('casual')
plt.ylabel('cnt')

plt.scatter(data['registered'], data['cnt'], color='blue')
plt.xlabel('registered')
plt.ylabel('cnt')

X = data['casual'].values.reshape(-1,1)
Y = data['cnt'].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
Model = LinearRegression()
Model.fit(X_train, y_train)

train_fit = Model.predict(X_train)
test_pred = Model.predict(X_test)

plt.scatter(X_train, y_train, color='gray')
plt.plot(X_train, train_fit, color='blue', linewidth=2)
plt.xlabel('casual')
plt.ylabel('cnt')

plt.scatter(X_test, y_test, color='gray')
plt.plot(X_test, test_pred, color='blue', linewidth=2)
plt.xlabel('casual')
plt.ylabel('cnt')

print('Mean Squared Error:', metrics.mean_squared_error(y_test, test_pred))  

# Graph with actual vs predicted

plt.scatter(X_test, y_test, color='gray')
plt.plot(X_test, test_pred, color='blue', linewidth=2)

#6a

from sklearn.linear_model import LogisticRegression

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
train_fit = Model.predict(X_train)
test_pred = Model.predict(X_test)

print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, test_pred)))

#6b


from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X, y = load_breast_cancer(return_X_y=True)
scale_x=preprocessing.scale(X)
X_train, X_test, y_train, y_test = train_test_split(scale_x, y, random_state=0)
Model= LogisticRegression()
Model.fit(X_train, y_train)
train_fit = Model.predict(X_train)
test_pred = Model.predict(X_test)
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, test_pred)))



#6c

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X, y = load_breast_cancer(return_X_y=True)
norm_x=preprocessing.normalize(X)
X_train, X_test, y_train, y_test = train_test_split(norm_x, y, random_state=0)
Model= LogisticRegression()
Model.fit(X_train, y_train)
train_fit = Model.predict(X_train)
test_pred = Model.predict(X_test)
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, test_pred)))











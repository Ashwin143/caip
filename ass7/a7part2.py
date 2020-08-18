#6
import sklearn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix 

# import csv using pandas
df = pd.read_csv(r"D:\\ML\\CAIP\\ass7\\Iris.csv")
# checking the data population
df.head(10)
#remove unnecessary id column
df.drop('Id',axis=1,inplace=True)
# checking rows and column
df.shape 
# checking correlation 
plt.figure(figsize=(7,4)) 
sns.heatmap(df.corr(),annot=True,cmap='cubehelix_r') #draws  heatmap with input as the correlation matrix calculted by(df.corr())
plt.show()
# from this we can figure out that petallength and width has max correlation and can be used that

# EDA

fig=df[df.Species=='Iris-setosa'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='orange', label='Setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='blue', label='versicolor',ax=fig)
df[df.Species=='Iris-virginica'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='green', label='virginica', ax=fig)
fig.set_xlabel("Petal Length")
fig.set_ylabel("Petal Width")
fig.set_title(" Petal Length VS Width")
fig=plt.gcf()
fig.set_size_inches(10,6)
plt.show()
#training the whole dataset 
train_X = train[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
train_y=train.Species
# output of training dataset
train_y.head(10)

#7

# splitting data into training and test

train, test = train_test_split(df, test_size = 0.3)
train_X = train[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]# taking the training data features
train_y=train.Species# output of our training data
test_X= test[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] # taking test data features
test_y =test.Species

# Accuracy Score for KNN Classifier using iris data
model=KNeighborsClassifier(n_neighbors=3) #this examines 3 neighbours for putting the new data into a class
model.fit(train_X,train_y)
prediction=model.predict(test_X)
print(metrics.accuracy_score(prediction,test_y))

#  Confusion matrix for KNN Classifier using iris data

results = confusion_matrix(test_y, prediction) 
print(results)


#8

import sklearn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
from sklearn import metrics
# import csv using pandas
df = pd.read_csv(r"D:\\ML\\CAIP\\ass7\\diabetes.csv")
# checking the data population
df.head(10)
# checking rows and column
df.shape 
# checking correlation 
plt.figure(figsize=(7,4)) 
sns.heatmap(df.corr(),annot=True,cmap='cubehelix_r') #draws  heatmap with input as the correlation matrix calculted by(df.corr())
plt.show()

regressor = LinearRegression()  
X = df['Age'].values.reshape(-1,1)
y = df['Outcome'].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()  
regressor.fit(X_train, y_train)
#  co-efficients of the linear model
print(regressor.coef_)
y_pred = regressor.predict(X_test)

plt.figure(figsize=(15,10))
plt.tight_layout()
sns.distplot(df['Outcome'])
#  Root Mean Square Error values 
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

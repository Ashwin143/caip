import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
data= pd.read_csv("xclara.txt",delimiter="\t")
print(data.head())
f1=data['V1'].values
f2=data['V2'].values

X=np.array(list(zip(f1,f2)))

kmeans=KMeans(n_clusters=3)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)


plt.scatter(f1,f2,c=y_kmeans,s=20,cmap='viridis')

centers=kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c="blue",s=200)
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
data= pd.read_csv("sample.csv")
print(data.head())
f1=data['x'].values
f2=data['y'].values
f3=data['z'].values


X=np.array(zip(f1,f2,f3))

kmeans=KMeans(n_clusters=3)
kmeans.fit(X)
y_kmeans=kmeans.predict(X)



#centers=kmeans.cluster_centers_

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

fig=plt.figure()
ax=plt.axes(projection='3d')
ax.scatter3D(f1,f2,f3,c=y_kmeans,cmap='viridis')

plt.show()






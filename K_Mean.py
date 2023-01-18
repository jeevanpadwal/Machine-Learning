import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd

dataset = load_iris()

x = dataset.iloc[:,[0,1,2,3]].values

from sklearn.cluster import KMeans
wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters= i,init= 'k - means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

# plotting results onto a graph allowing us to observe 'The elbow'

plt.plot(range(1,11),wcss)
plt.title('The elbow method')
plt.xlable('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters= i,init= 'k - means++',max_iter=300,n_init=10,random_state=0)
y_kmeans = kmeans.fit_predict(x)

plt.scatter([y_kmeans == 0,0],x[y_kmeans ==0,1],s= 100,c ='red',label = 'Iris-sentosa')

plt.scatter([y_kmeans == 1,0],x[y_kmeans ==1,1],s= 100,c ='blue',label = 'Iris-versicolour')

plt.scatter([y_kmeans == 2,0],x[y_kmeans ==2,1],s= 100,c ='green',label = 'Iris-virginica')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s = 100,c = 'yellow',label = 'Centroids')

plt.legend()

plt.show()



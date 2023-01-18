
import numpy as np
import pandas as pd
from copy import deepcopy
from matplotlib import pyplot as plt


def MKMean():
    print("_____________________________")
    #set the three centres,the model should predict similer results

    center_1 = np.array([1,1])
    print(center_1)

    print("____________________________________")
    center_2 = np.array([5,5])
    print(center_2)

    print("____________________________________")
    center_3 = np.array([8,1])
    print(center_3)

    #generate random data and center it to the three centers
    data_1 = np.random.randn(7,2) + center_1
    print("Elementes of first cluster with size"+str(len(data_1)))
    print(data_1)

    print("__________________________________________")
    data_2 = np.random.randn(7,2) + center_2
    print("Elementes of second cluster with size"+str(len(data_2)))
    print(data_2)

    print("_______________________________________")
    data_3 = np.random.randn(7,2) + center_3
    print("Elementes of third cluster with size"+str(len(data_3)))
    print(data_3)

    print("____________________________________________")
    data = np.concatenate((data_1,data_2,data_3),axis =0)
    print("Size of complete dataset"+str(len(data)))
    print(data)

    print("____________________________________________")
    plt.scatter(data[:,0],data[:,1],s =7)
    plt.title(" Input Dataset")
    plt.show()

    print("_____________________________________________")
    #Number of clusters
    k = 3

    #number of traning data
    n = data.shape[0]
    print("Total number of elements are",n)

    print("______________________________________________")
    #number of features in the data
    c = data.shape[1]
    print("Total number of features are",c)
    print("______________________________________________")
    #generate random centers here we use sigma and mean to ensure it represent the whole data
    mean = np.mean(data,axis =0)
    print("Values of mean",mean)
    
    print("___________________________________________")
    # calculate standerd deviation
    std = np.std(data,axis =0)
    print("Value of std",std)

    print("_____________________________________________")
    centers = np.random.randn(k,c)*std + mean
    print("Random points are ",centers)

    print("__________________________________________")
    # plot the data and the centers genrated as random
    plt.scatter(data[:,0],data[:,1],c ='r',s=7)
    plt.scatter(centers[:,0],centers[:,1],marker = '*',c = 'g',s = 150)
    plt.title('Input Dataset with random centroid *')
    plt.show()
    
    print("____________________________________________")

    centers_old = np.zeros(centers.shape) # to store old centers
    centers_new = deepcopy(centers)        #Store new centers

    print("Values of old centroids")
    print(centers_old)
    print("______________________________________")
    
    print("Values of new centroids ")
    print(centers_new)
    print("__________________________________________")

    data.shape
    clusters = np.zeros(n)
    distances = np.zeros((n,k))

    print("________________________________________________")

    error = np.linalg.norm(centers_new - centers_old)
    print("value of error is",error)

    #when after an update the estimate of that center stays the same, exit loop 
    while error != 0:
        print("Values of error is",error)
        #measure the distance to every center
        print("Measure the distance of the every center")

        for i in range(k):
            print("Iteration number",i)
            distances[:,i] = np.linalg.norm(data - centers[i],axis = 1)

       #Assign all traning data to closest center
        clusters = np.argmin(distances,axis = 1)

        centers_old = deepcopy(centers_new)

        #calculate mean for every cluster and update the center 
        for i in range(k):
            centers_new[i] = np.mean(data[clusters == i],axis =0)
        error = np.linalg.norm(centers_new - centers_old)

    # end of while
    centers_new

    #plot the data and the centers genraed as random
    plt.scatter(data[:,0],data[:,1],s=7)
    plt.scatter(centers_new[:,0],centers_new[:,1],marker ='*',c ='g',s = 150)
    plt.title('Final Data with Centroids ')
    plt.show()

def main():

    print("Unsupervised Machinelearning")
    print("CLustering using K Mean Algoritham")

    MKMean()

if __name__ == "__main__":
    main()
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection  import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier



def main():

    data = pd.read_csv("PlayPredictor.csv")
    data.head()

    #Data_train,Data_test,Target_train,Target_test = train_test_split(Data1,Target,test_size=0.5)

   

if __name__ == "__main__":
    main()
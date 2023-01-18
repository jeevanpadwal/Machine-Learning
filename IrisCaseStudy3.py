from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection  import train_test_split
from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)

class MarvellousKneighborsClassifier:

    def fit(self, trainingdata, traningtarget):
        self.TraningData = trainingdata
        self.TraningTarget = traningtarget

    def closest(self, row):
        minimumdistance = euc(row, self.TraningData[0])
        minimumindex = 0

        for i in range(1,len(self.TraningData)):
            Distance = euc(row , self.TraningData[i])
            if Distance < minimumdistance:
                minimumdistance = Distance
                minimumindex = i

        return self.TraningTarget[minimumindex]

    def predict(self, TestData):
        predictions = []

        for value in TestData:
            result = self.closest(value)
            predictions.append(result)

        return predictions


def MarvellousML():
    Dataset = load_iris()  # 1) Load the data 

    Data = Dataset.data
    Target = Dataset.target

    # 2) Manipulet the data
    Data_train,Data_test, Target_train, Target_test = train_test_split(Data, Target, test_size= 0.5)

    Classifier = MarvellousKneighborsClassifier()
    
    #3) Built the model
    Classifier.fit(Data_train,Target_train)

    #4) Test the model
    Predictions = Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test, Predictions)

    #5) Improvr -- Missing

    return Accuracy

def main():

    ret = MarvellousML()

    print("Accuracy Of Iris Dataset with KNN is ", ret * 100)


if __name__=="__main__":
    main()
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

def SVM():
    
    #load dataset
    cancer = datasets.load_breast_cancer()
    
    #print the names of 13 features
    print("Features of the cancer dataset :",cancer.feature_names)
    
    #print the lable type of cancer('malignant' 'benign')
    print("Lables of the data set :",cancer.target_names)
    
    #print the data(feature) shape
    print(" Shape fo dataset is :",cancer.data.shape)
    
    #print the cancer data features (top 5 records)
    print("First 5 records are :")
    print(cancer.data[0:5])
    
    #print the cancer labels (0:malingnant, 1:beningn)
    print("Target of dataset :",cancer.target)
    
    #Split dataset into traning set and test set
    
    X_train, X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,test_size=0.3,random_state=109)#70 % test and 30 % test
    
    #create svm classifier
    clf = svm.SVC(kernel='linear')#linear Kernel
    
    #train the model using the traning sets
    clf.fit(X_train,y_train)
    
    #predict the responce for test dataset
    y_pred = clf.predict(X_test)
    
    #model accuracy : how often is the classifier correct
    print("Accuracy of the model is :",metrics.accuracy_score(y_test,y_pred)*100)
    
    
def main():
    print("-----------Support Vector Machine---------------")
    
    SVM()
    
if __name__ =="__main__":
    main()
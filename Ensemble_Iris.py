from sklearn.ensemble import AdaBoostClassifier
from sklearn import datasets

#import train_test_split function
from sklearn.model_selection import train_test_split

#Import scikit-learn metrics module for accuracy calculation 
from sklearn import metrics

#Load data

iris = datasets.load_iris()

X = iris.data
y = iris.target

#Split dataset into traning set and test set
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)#70% traning and 30%testing

abc = AdaBoostClassifier(n_estimators =50,learning_rate=1)

#traning Adaboost classifier
model = abc.fit(X_train, y_train)

y_predict = model.predict(X_test)

print("Accuracy :",metrics.accuracy_score(y_test,y_predict))
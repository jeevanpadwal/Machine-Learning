#pip install scikit-learn

from sklearn import tree

#Rough 1
#Smooth 0

#Tenis 1
#Cricket 2

Feachers = [[35,1],[47,1],[90,0],[48,1],[90,0],[92,0],[35,1],[35,1],[35,1],[92,0],[45,1]]
Lables = [1,1,1,1,2,2,1,2,1,1,1,2,1]

obj = tree.DecisionTreeClassifier()

obj = obj.fit(Feachers,Lables)

print(obj.predict([[97,0]]))



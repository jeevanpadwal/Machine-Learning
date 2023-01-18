#pip install scikit-learn

from sklearn import tree

#Rough 1
#Smooth 0

#Tenis 1
#Cricket 2
def BallPredictor(Weight , Surface):
    
    Feachers = [[35,1],[47,1],[90,0],[48,1],[90,0],[92,0],[35,1],[35,1],[35,1],[92,0],[45,1]]
    Lables = [1,1,1,1,2,2,1,2,1,1,1,2,1]

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(Feachers,Lables)

    ret = (obj.predict([[Weight,Surface]]))
    
    if ret == 1:
        print("Your object looks like Tenis Ball")
    else:
        print("Your object looks like cricket BAll")

def main():
    print("________Ball Predictor Case Study _________")
    
    print("Please enter weight of your object in grams")
    weight = int(input())
    
    print("Please Enter type of surfsec of your object(Rough/Smooth)")
    surface = input()
    
    if surface.lower() =="rough":
        surface =1
    elif surface.lower() =="smooth":
        surface=0
    else:
        exit()
    
    
    BallPredictor(weight,surface)
    


if __name__ =="__main__":
    main()
from sklearn.datasets import load_iris


def main():

    Iobj = load_iris()

    print("Features of iris ")
    print(Iobj.feature_names)


    for i in range(1,len(Iobj.target)):
        print("ID :%d, Lable %s,Feature:%s"%(i,Iobj.data[i],Iobj.target[i]))

if __name__ == "__main__":
    main()
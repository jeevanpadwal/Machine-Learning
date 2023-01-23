import pandas as pd

from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error

def HeadBrainPredictor():
    data = pd.read_csv('MarvellousHeadBrain.csv')
    
    print("Size if data set",data.shape)
    
    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values
    
    X = X.reshape((-1,1))
    
    n = len(X)
    
    reg = LinearRegression()
    
    reg = reg.fit(X,Y)
    
    y_pred = reg.predict(X)
    
    r2 = reg.score(X,Y)
    
    print(r2)
    
    
def main():
    
    HeadBrainPredictor()
    
if __name__ =="__main__":
    main()
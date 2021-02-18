import numpy as np
class LinearRegression():
    def __init__(self,lr=0.001,n_inters=1000):
        self.lr = lr
        self.n_inters = n_inters
        self.weight = None
        self.bias = None
    
    
    
    def fit(self,X,y):
        n_samples,n_feature = X.shape
        self.weight = np.zeros(n_feature)
        self.bias = 0
        for _ in range(self.n_inters):
            y_predicted = np.dot(X,self.weight) + self.bias
            dw = (1/n_samples) * np.dot(X.T,(y_predicted-y))
            db = np.mean(y_predicted-y)

            self.weight -= self.lr * dw
            self.bias -= self.lr * db


    def predict(self,X):
        y_predicted = np.dot(X,self.weight) + self.bias
        return y_predicted

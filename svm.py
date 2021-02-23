
import numpy as np
class SVM():
    def __init__(self,lr = 0.001,lambda_params =0.01,n_iters=1000):
        self.lr = lr
        self.lambda_params = lambda_params
        self.n_iters = n_iters
        self.weight = None
        self.bias = None
    def fit(self,X,y):
        n_samples,n_features = X.shape
        self.weight = np.zeros(n_features)
        self.bias = 0
        y_ = np.where(y<=0,-1,1) 
        
        for _ in range(self.n_iters):
            for idx,x_i in enumerate(X):
                condition = y_[idx] * (np.dot(x_i,self.weight) - self.bias) >= 1
                if condition:
                    self.weight -= self.lr * (2 * self.lambda_params * self.weight)
                else:
                    self.weight -= self.lr * (2* self.lambda_params * self.weight - np.dot(x_i,y_[idx]))

                    self.bias -= self.lr * y_[idx]
                
    def predict(X):
        linear_output = np.dot(X,self.weight) - self.bias
        return np.sign(linear_output)

import numpy as np


class Perceptron():
    def __init__(self, lr=0.001, n_iters=1000):
        self.weights = None
        self.bias = None
        self.lr = lr
        self.n_iters = n_iters
        self.activation_func = self.unit_step_functions

    def fit(self, X, y):
        n_samples, n_features = X.shape 
        self.weights = np.zeros(n_features)
        self.bias = 0
        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)
                # print(type(y_predicted))
                # print(y_predicted.shape)
                update = self.lr * (y_[idx]-y_predicted)
                self.weights += update*x_i
                self.bias += update

    def predict(self, X):
        linear_layout = np.dot(X, self.weights) + self.bias
        y_predict = self.activation_func(linear_layout)
        # print(type(y_predict))
        # print(y_predict.shape)
        return y_predict

    def unit_step_functions(self, x):
        return np.where(x >= 0, 1, 0)

import numpy as np


class LogisticRegression():
    def __init__(self, lr=0.01, inters=1000):
        self.lr = lr
        self.inters = inters
        self.bias = None
        self.weight = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        print(X.shape)
        self.weight = np.zeros(n_features)
        self.bias = 0
        for _ in range(self.inters):
            linear_model = np.dot(X, self.weight) + self.bias
            y_predicted = self.sigmoid(linear_model)
            print(linear_model.shape)
            dw = (1/n_samples) * np.dot(X.T, (y_predicted-y))
            db = (1/n_samples) * np.sum(y_predicted -y)

            self.weight -= dw*self.lr
            self.bias -= db*self.lr

    def predict(self, X):
        linear_model = np.dot(X, self.weight) + self.bias
        y_predict = self.sigmoid(linear_model)
        y_predic_cls = [1 if i > 0.5 else 0 for i in y_predict]
        return y_predic_cls

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

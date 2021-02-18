import numpy as np
from collections import Counter
def euclidean(x1,x2):
    print(x1,x2)
    return np.sqrt(np.sum((x1-x2)**2))
class KNN():
    def __init__(self,k = 3):
        self.k = k
    def fit(self,X,y):
        self.X_train = X
        self.y_train =y
    def predict(self,X):
        predictedlables = [self._predict(x) for x in X]
        return np.array(predictedlables)
    def _predict(self,x):
        print(type(self.X_train),type(self.X_train[0]))
        distances = [euclidean(x,x_train) for x_train in self.X_train ]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_lables = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_lables).most_common(1)
        return most_common[0][0]


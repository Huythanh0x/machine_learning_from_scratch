import numpy as np
from collections import Counter
from decisiontree import DecisionTree

def bootstrap_sample(X,y):
    n_samples = X.shape[0]
    indexs = np.random.choice(n_samples,n_samples,replace=True)
    return X[indexs],y[indexs]

def most_common_label(y):
    counter = Counter(y)
    most_common = counter.most_common(1)[0][0]
    return most_common


class RandomForest:
    
    def __init__(self,n_trees=1000,min_samples_split=2,max_depth=100,n_feature=None):
        self.n_trees = n_trees
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_feature = n_feature
        self.trees = []
    def fit(self,X,y):
        self.tree = []
        for _ in range(self.n_trees):
            tree = DecisionTree(min_samples_split=self.min_samples_split,max_depth=self.max_depth,n_features=self.n_feature)
            x_sample,y_sample = bootstrap_sample(X, y)
            tree.fit(x_sample,y_sample)
            self.trees.append(tree)
    def predict(self,X):
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        tree_preds = np.swapaxes(tree_preds,0,1)
        y_pred = [most_common_label(tree_pred) for tree_pred in tree_preds]
        return np.array(y_pred)
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from randomforest import RandomForest

def accuracy(y_true,y_predict):
    acc = np.sum(y_true==y_predict)/len(y_true)
    return acc
data = datasets.load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=22)

clf = RandomForest(n_trees=3,max_depth=10)
clf.fit(X_train,y_train)
predictions = clf.predict(X_test)

print(accuracy(y_test,predictions))
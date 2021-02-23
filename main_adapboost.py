import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

from adapboost import Adaboost

def accuracy(y_true,y_pred):
    accuracy = np.sum(y_true==y_pred) / len(y_true)
    return accuracy
data = datasets.load_breast_cancer()
X = data.data
y = data.target

y[y==0] = -1
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

clf = Adaboost(n_clf = 6)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy(y_test,y_pred)
print(accuracy)
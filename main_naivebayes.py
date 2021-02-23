import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from naivebayes import NaiveBayes

def accuracy(y_true,y_predic):
    accuracy = np.sum(y_true==y_predic)/len(y_true)
    return accuracy

X,y = datasets.make_classification(n_samples = 1000,n_features=50,n_classes=2,random_state=1000)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4,random_state=1000)

nb = NaiveBayes()
nb.fit(X_train,y_train)
predictions = nb.predict(X_test)

print(accuracy(y_test,predictions))
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000','00FF00','0000FF'])

iris = datasets.load_iris()
X,y = iris.data,iris.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.4,random_state =1000)
list_k =[]
list_accuracy = []
from knn import KNN
for k in range(1,2):
    clf = KNN(k)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    accuracy = np.sum(predictions == y_test)/len(y_test)
    list_k.append(k)
    list_accuracy.append(accuracy)

plt.plot(list_k, list_accuracy)
plt.title('Accuracy')
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.show()

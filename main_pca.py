from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

from pca import PCA

data = datasets.load_iris()
X = data.data
y = data.target

pca = PCA(n_components=2)
pca.fit(X)
x_projected = pca.transform(X)

print('Shape of X:',X.shape)
print('Shape of transform X:',x_projected.shape)


x1 = x_projected[:,0]
x2 = x_projected[:,1]

plt.scatter(x1,x2,c=y,edgecolor = 'none',alpha= 0.8,cmap=plt.cm.get_cmap('viridis',3))
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.colorbar()
plt.show()
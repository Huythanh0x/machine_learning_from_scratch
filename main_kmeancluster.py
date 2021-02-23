import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as pyplot

from kmeancluster import KMeans

X,y = make_blobs(centers = 3,n_samples = 500,n_features=2,shuffle = True)
print(X.shape)

clusters = len(np.unique(y))
print(clusters)

k = KMeans(K = clusters,max_iters=150,plot_steps=True)

k.predict(X) 
k.plot
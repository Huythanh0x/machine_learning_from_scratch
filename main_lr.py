import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

X,y = datasets.make_regression(n_samples=10,n_features=1,noise=1,random_state=4)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1000)

# fig = plt.figure(figsize=(8,16))
# plt.scatter(X[:,0],y,color='b',marker='o',s=30)
# plt.show()
from lr import LinearRegression



def mse(actual_y,y_predicted):
    return np.mean((actual_y-y_predicted)**2)


regression  = LinearRegression(lr = 0.01)
regression.fit(X_train,y_train)
predictions = regression.predict(X)
mse_value = mse(y,predictions)
print(mse_value)


cmap = plt.get_cmap('viridis')
fig = plt.figure(figsize=(8,6))
m1 = plt.scatter(X,y,color=cmap(0.9),s=10)
plt.plot(X,predictions,color='black',linewidth=2,label="Prediction")
plt.show()
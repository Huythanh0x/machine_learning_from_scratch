import csv
import numpy as np
import pandas as pd

#slow way
FILE_NAME = "spambase.data"
with open (FILE_NAME,'r') as f:
    data = list(csv.reader(f,delimiter=","))
data = np.array(data)

print(data.shape)

n_samples,n_features = data.shape
n_features -= 1
X = data[:,0:n_features]
y = data[:,n_features]

print(X.shape,y.shape)

#faster way 
data = np.loadtxt(FILE_NAME,delimiter=",")

print(data.shape)

n_samples,n_features = data.shape
n_features -= 1
X = data[:,0:n_features]
y = data[:,n_features]

print(X.shape,y.shape)

#faster way 
data = np.genfromtxt(FILE_NAME,delimiter=",")

print(data.shape)

n_samples,n_features = data.shape
n_features -= 1
X = data[:,0:n_features]
y = data[:,n_features]

print(X.shape,y.shape)

#use pandas

df = pd.read_csv(FILE_NAME,delimiter=",")
data = df.to_numpy()
print(data.shape)

n_samples,n_features = data.shape
n_features -= 1
X = data[:,0:n_features]
y = data[:,n_features]

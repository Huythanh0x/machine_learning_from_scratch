import numpy as np
predictions = [1,1,1,1,1,-1,-1,1,1]
y = [-1,-1,-1,-1,1,-1,-1,1,1]
predictions = np.array(predictions)
y = np.array(y)
print(np.exp(0.3*-predictions*y))
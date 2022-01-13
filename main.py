import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=0)
y = y.reshape((y.shape[0], 1))

print('dimensions de x : ', X.shape)
print('dimensions de y : ', y.shape)


plt.figure(facecolor="#191919")
plt.axes().set_facecolor("#191919")
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='summer')
plt.show()
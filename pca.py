import numpy as np


class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        self.mean = np.mean(X, axis=0)
        X = X - self.mean
        #center data points
        cov = np.cov(X.T)
        # cov feature
        eigenvalues, eigenvectors = np.linalg.eig(cov)
        eigenvectors = eigenvectors.T
        # find eigenvalues,eigenvectors
        indexs = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[indexs]
        eigenvectors = eigenvectors[indexs]
        #sort index by eigenvector
        self.components = eigenvectors[0:self.n_components]

    def transform(self, X):
        X = X - self.mean
        return np.dot(X, self.components.T)
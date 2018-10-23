# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 12:20:52 2018

@author: 小周

"""

'''
=============================================================
Large scale machine learning and stochastic gradient descent
随机梯度下降
=============================================================
'''

import numpy as np
from numpy.random import seed
import matplotlib.pyplot as plt
import iris

class AdaptLinearSGD(object):
    '''Adaptive Linear Neuron classifier
    
    Parameters
    ------------
    eta: float
        Learning rate (between 0.0 and 1.0)
    n_iter: int
        Passes over the training dataset.
        
    Attributes
    ------------
    w_: id-array
         Weights after fitting.(训练的的权重值)
    cost_ : list
        Sum-of-squares cost function value averaged over all
        training samples in each epoch.
    shuffle : bool (default: True)
        Shuffles training data every epoch if True to prevent cycles.
    random_state : int (default: None)
        Set random state for shuffling and initializing the weights.
    '''
    def __init__(self, eta=0.1, n_iter=10, shuffle=True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.w_initialized = False
        self.shuffle = shuffle
        if random_state:
            seed(random_state)
    
    def fit(self, X, y):
        '''Fitting the training data
        
        Parameter
        -----------
        X : {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples and
            n_features is the number of features.
        y : array-like, shape = [n_samples]
            Target values.

        Returns
        -------
        self : object
        '''
        self._initialize_weights(X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle(X, y)
            cost = []
            for xi, target in zip(X, y):
                cost.append(self._update_weights(xi, target))
            avg_cost = sum(cost) / len(y)
            self.cost_.append(avg_cost)
        return self
    
    def partial_fit(self, X, y):
        '''Fit training data without reinitializing the weights'''
        if not self.w_initialized:
            self._initialize_weights(X.shape[1])
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, target)
        else:
            self.update_weights(X, y)
        return self
    
    def _shuffle(self, X, y):
        '''Shuffle training data'''
        r = np.random.permutation(len(y))
        return X[r], y[r]
    
    def _initialize_weights(self, m):
        '''Initialize weights to zeros
        
        Parameters
        ------------
        m: X的维度
        
        '''
        self.w_ = np.zeros(1 + m) # Add w_0
        self.w_initialized = True
        
    def _update_weights(self, xi, target):
        '''Apply Adaptive Linear learning rule to update the weights
        
        Returns:
        ----------
        cost
        
        '''
        output = self.net_input(xi)
        error = (target - output)
        self.w_[1:] += self.eta * xi.dot(error)
        self.w_[0] += self.eta * error
        cost = 0.5 * error**2
        return cost

    def net_input(self, X):
        '''Calculate net input'''
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def activation(self, X):
        '''Compute linear activation'''
        return self.net_input(X)
    
    def predict(self, X):
        '''Return class label after unit step'''
        return np.where(self.activation(X) >= 0.0, 1, -1)

def test():
    X, y = iris.load_iris()
    X_std = np.copy(X)
    X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()

    ada = AdaptLinearSGD(n_iter=15, eta=0.01, random_state=1)
    ada.fit(X_std, y)
    
    iris.plot_decision_region(X_std, y, classifier=ada)
    plt.title('Adaline - Stochastic Gradient Descent')
    plt.xlabel('sepal length [standardized]')
    plt.ylabel('petal length [standardized]')
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.show()
    
    plt.plot(range(1, len(ada.cost_) + 1), ada.cost_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Average Cost')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    test()













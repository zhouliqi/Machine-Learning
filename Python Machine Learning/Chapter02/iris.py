# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 20:59:40 2018

@author: 小周

"""

# 分类iris数据

'''
=========================================================
The Iris Dataset
=========================================================
This data sets consists of 3 different types of irises'
(Setosa[50], Versicolour[50], and Virginica[50]) petal and sepal
length, stored in a 150x4 numpy.ndarray
The rows being the samples and the columns being:
Sepal Length[0], Sepal Width[1], Petal Length[2] and Petal Width[3].
See `here <https://en.wikipedia.org/wiki/Iris_flower_data_set>`_ for more
information on this dataset.
'''
#print(__doc__)

#import pandas as pd
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# 感知器学习算法
class Perceptron(object):
    '''Preceptron classifier
    
    Parameters
    ------------
    eta:float
        learning rate(between 0.0 and 1.0)
    n_iter:int
        Passes over the training dataset.
    shuffle: bool (default: True)
        Shuffles training data every epoch if True to prevent cycles.
    random_state: int (default: None)
        Set random state for shuffling and initializing the weights.
        
    Attributes
    ------------
    w_: 1d-array
        weights after fitting
    errors_: list
        Number of misclassifications in every eopch
    '''
    
    def __init__(self, eta=0.01, n_iter=10, shuffle=True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.shuffle = shuffle
        if random_state:
            np.random.seed(random_state)
    
    def fit(self, X, y):
        '''Fit training data
        
        Parameters
        ------------
        X: {array-like}, shape=[n_samples, n_features]
            Training vectors, where n_samples is the number of samples
            and n_features is the number of features
        y: array-like, shape=[n_samples]
            Target values
            
        Return
        ------------
        self.object
        '''
        
        self.w_ = np.zeros(1 + X.shape[1]) # Add w_0
        self.errors_  = []
        
        for _ in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle(X, y)
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
    
    def _shuffle(self, X, y):
        '''Shuffle training data'''
        r = np.random.permutation(len(y))
        return X[r], y[r]
    
    def net_input(self, X):
        '''Calculate net input'''
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def predict(self, X):
        '''Return class label after unit step
            Setosa: 1
            Versicolor: -1
        '''
        return np.where(self.net_input(X) >= 0.0, 1, -1)

# 画出errors曲线
def plot_errors(classifier):
    plt.plot(range(1, len(ppn.errors_) + 1), classifier.errors_, marker='o')
    plt.xlabel('Epoches')
    plt.ylabel('Number of misclassifications')
    plt.show()

# 画出iris数据的散点图
def plot_iris_data(X):
    '''Plot the data of iris'''
    plt.scatter(X[:50, 0], X[:50, 1], color='green', marker='*', label='setosa')
    plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
    plt.xlabel('petal length')
    plt.ylabel('sepal length')
    plt.legend(loc='upper left')
    plt.show()


# 画出决策边界
def plot_decision_region(X, y, classifier, resolution=0.02):
    markers = ('s', 'x', 'o','^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx), marker=markers[idx], label=cl)
        
# 加载数据
def load_iris():
    '''Load the dataset of iris'''
    iris = datasets.load_iris()
    iris_x, iris_y = iris.data, iris.target
    X = np.hstack((iris_x[:100, 0:1], iris_x[:100, 2:3]))
    y = iris_y[:100]
    y[:50] = -1
    return X, y

if __name__ == '__main__':
    
    X, y = load_iris()
    
    '''
    df = pd.read_csv('https://raw.githubusercontent.com/rasbt/python-machine-learning-book/master/code/datasets/iris/iris.data', header=None)
    df.tail()
    y = df.iloc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)
    X = df.iloc[0:100, [0, 2]].values'''
    

    # 画出iris的散点图
    plot_iris_data(X)
    
    ppn = Perceptron(eta = 0.1, n_iter = 10)
    ppn.fit(X,y)
    print(ppn.w_)
    # 
    plot_errors(ppn)
    #print(ppn.w_)
   
    
    plot_decision_region(X, y, classifier=ppn)
    plt.xlabel('sepal length [cm]')
    plt.ylabel('petal length [cm]')
    plt.legend(loc='upper left')
    plt.show()







# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 10:11:25 2018

@author: 小周

"""

'''
================================================
Implementing an adaptive linear neuron in Python
Gradient Descent(梯度下降)
================================================
'''

import numpy as np
import matplotlib.pyplot as plt
import iris


class AdaptLinearGD(object):
    '''Adaptive Linear Neuron classifier.
    
    Parameters
    ------------
    eta: float
        Learning rate (between 0.0 and 1.0)
    n_iter: int
        Passes over the training dataset
    
    Attributes
    ------------
    w_: 1d-array
        Weights after fitting
    cost_: list
        Sum-of-squares cost function value in each epoch.
    
    '''
    
    def __init__(self, eta=0.1, n_iter=50):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, y):
        '''Fitting the data.
        
        Parameters
        -------------
        X : {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples and
            n_features is the number of features
        y : array-like, shape = [n_samples]
            Traget values
        
        Returns
        ----------
        self : object
        
        '''
        self.w_ = np.zeros(1 + X.shape[1]) # Add w_0
        self.cost_ = []
        
        for i in range(self.n_iter):
            #net_input = self.net_input(X)
            # 请注意’activation‘方法在代码没有作用，它只是个identity函数
            # 我们可以直接写成’output = self.net_input(X)‘
            # activation的目的是使其更具有概念性，例如：在Logistic回归中，
            # 我们应该把它转化为sigmod函数来实现一个Logistic回归分类器
            output = self.activation(X)
            errors = (y - output)
            self.w_[1:] +=self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost_.append(cost)
        return self
    
    def net_input(self, X):
        '''Ccalculate net input'''
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def activation(self, X):
        '''Compute linear activation'''
        return self.net_input(X)
    
    def predict(self, X):
        '''Return class label after unit step'''
        return np.where(self.activation(X) >= 0.0, 1, -1)

# 画errors曲线
def plot_errors():
    figure, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
    X, y = iris.load_iris()
    ada1 = AdaptLinearGD(n_iter=10, eta=0.01).fit(X, y)
    print(ada1.w_)
    
    ax[0].plot(range(1, len(ada1.cost_) + 1), np.log10(ada1.cost_), marker='o')
    ax[0].set_xlabel('Epoches')
    ax[0].set_ylabel('log(Sum-squared-error)')
    ax[0].set_title('Adapt Linear Learning rate 0.01')
    
    ada2 = AdaptLinearGD(n_iter = 10, eta=0.0001,).fit(X, y)
    ax[1].plot(range(1, len(ada2.cost_) + 1), ada2.cost_, marker='o')
    ax[0].set_xlabel('Epoches')
    ax[0].set_ylabel('log(Sum-squared-error)')
    ax[0].set_title('Adapt Linear Learning rate 0.0001')
    plt.tight_layout()
    plt.show()


def AdaptLinearGDTest():
    '''AdaptLinearGD类的测试函数'''
    X, y = iris.load_iris()
    X_std = np.copy(X)
    X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()
    
    ada = AdaptLinearGD(n_iter=10, eta=0.01)
    ada.fit(X_std, y)
    
    # 画出分类的区域
    iris.plot_decision_region(X_std, y, classifier=ada)
    plt.title('Adapt Linear - Gradient Descent')
    plt.xlabel('sepal length [standardized]')
    plt.ylabel('petal length [standardized]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
    
    # 画出errors曲线
    plt.plot(range(1, len(ada.cost_) + 1), ada.cost_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Sum-squared-error')
    plt.tight_layout()
    plt.show()
    
#===========================================================================
    
# 采用Logistic回归
class LogisticRegressionGD(AdaptLinearGD):
    def __init__(self, eta=0.01, n_iter=50):
        AdaptLinearGD.__init__(self, eta, n_iter)
    def fit(self, X, y):
        # 和基类的大体一致，不过这里用的是Logistic ’cost‘
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []
        
        for i in range(self.n_iter):
            #net_input = self.net_input(X)
            output = self.activation(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            
            # 注意在这里我们计算的是Logistic的’cost‘
            # 而不是sum of squared errors cost
            cost = -y.dot(np.log(output)) - ((1 - y).dot(np.log(1 - output)))
            self.cost_.append(cost)
        return self
    def predict(self, X):
        # We use the more common convention for logistic
        # regression returning class label 0 and 1
        # instead of -1 and 1. Also, the threshold(阈值) then 
        # change from 0.0 to 0.5
        return np.where(self.activation(X) >= 0.5, 1, 0)
    
    # The Content of 'activation' changed
    # from linear (AdaptLinearGD) to sigmod.
    # Note that this method is now return the 
    # probability of the positive class
    # also "predict_prob" in scikit-learn
    def activation(self, X):
        '''Compute sigmod activation.'''
        z = self.net_input(X)
        sigmod = 1.0 / (1.0 + np.exp(-z))
        return sigmod

def  LogisticRegressionGDTest():
    '''AdaptLinearLogisticGD类的测试函数'''
    from sklearn import datasets
    iris = datasets.load_iris()
    X, y = iris.data[:100, [0, 2]], iris.target[:100]
    
    X_std = np.copy(X)
    X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()
    '''X, y = iris.load_iris()
    X_std = np.copy(X)
    X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()'''
    
    lr = LogisticRegressionGD(n_iter=25, eta=0.15)
    lr.fit(X_std, y)
    
    iris.plot_decision_region(X_std, y, classifier=lr)
    plt.title('Logistic Regression - Gradient Descent')
    plt.xlabel('sepal length [standardized]')
    plt.ylabel('sepal width [standardized]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    
    plt.show()
    
    plt.plot(range(1, len(lr.cost_) + 1), lr.cost_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Logistic Cost')
    
    plt.tight_layout()
    plt.show()
    
    
if __name__ == '__main__':
    
    #plot_errors()
    #AdaptLinearGDTest()
    LogisticRegressionGDTest()
    
    
    
    
    
    
    
    
    
    
    
    
    
    


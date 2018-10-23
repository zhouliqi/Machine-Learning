# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 23:43:21 2018

@author: 小周

"""

'''
====================================================
Modeling class probabilities via logistic regression
====================================================
'''

# 1: Logistic regression intuition and conditional probabilities
import numpy as np
import matplotlib.pyplot as plt

def sigmod(z):
    return 1.0 / (1.0 + np.exp(-z))

def plot_sigmod_function():
    # 画sigmod函数图像
    z = np.arange(-7, 7, 0.1)
    phi_z = sigmod(z)
    
    plt.plot(z, phi_z)
    plt.axvline(0, 0, color='k')
    plt.ylim(-0.1, 1.1)
    plt.xlabel('z')
    plt.ylabel('$\phi (z)$')
    
    # y axis ticks and gridline
    plt.yticks([0.0, 0.5, 1.0])
    ax = plt.gca()
    ax.yaxis.grid(True)
    plt.tight_layout()
    plt.show()


# 2: Learning the weights of the logistic cost function
def cost_1(z):
    return -np.log(sigmod(z))

def cost_0(z):
    return -np.log(1 - sigmod(z))

def plot_cost_function():
    # 画出代价函数图像
    z = np.arange(-10, 10, 0.1)
    phi_z = sigmod(z)
    
    c1 = [cost_1(x) for x in z]
    plt.plot(phi_z, c1, label='J(w) if y=1')

    c0 = [cost_0(x) for x in z]
    plt.plot(phi_z, c0, linestyle='--', label='J(w) if y=0')
    
    plt.ylim(0.0, 5.1)
    plt.xlim([0, 1])
    plt.xlabel('$\phi$(z)')
    plt.ylabel('J(w)')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
    
# 3: Training a logistic regression model with scikit-learn

# 3.1: 数据导入和预处理
from sklearn import datasets
import First_scikit_learn
iris = datasets.load_iris()
X = iris.data[:, [2, 3]] # 获取iris数据集的第三列和第四列数据
y = iris.target
# Splitting data into 70% training and 30% test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# Standardizing the features:
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train) # Compute the mean and std to be used for later scaling
X_train_std = sc.transform(X_train) # Perform standardization by centering and scaling
X_test_std = sc.transform(X_test)
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

def Logistic():
    
    # 3.2: 训练分类器
    from sklearn.linear_model import LogisticRegression
    
    lr = LogisticRegression(C=1000.0, random_state=0)
    lr.fit(X_train_std, y_train)
    
    First_scikit_learn.plot_decision_regions(X_combined_std, y_combined, classifier=lr, test_idx=range(105, 150))
    plt.xlabel('petal length [standardized]')
    plt.ylabel('petal width [standardized]')
    plt.legend(loc='upper left')
    plt.title('Logistic Regression')
    plt.tight_layout()
    plt.show()

# Tackling overfitting via regularization
def plot_fitting():
    from sklearn.linear_model import LogisticRegression
    weights, params = [], []
    for c in np.arange(-5., 5.):
        lr = LogisticRegression(C=10.**c, random_state=0)
        lr.fit(X_train_std, y_train)
        weights.append(lr.coef_[1])
        params.append(10**c)
    weights = np.array(weights)
    plt.plot(params, weights[:, 0], label='petal length')
    plt.plot(params, weights[:, 1], label='petal width')
    plt.ylabel('weight coefficient')
    plt.xlabel('C')
    plt.legend(loc='upper left')
    plt.xscale('log')
    plt.show()

if __name__ == '__main__':
    #plot_sigmod_function()
    #plot_cost_function()
    Logistic()
    #plot_fitting()












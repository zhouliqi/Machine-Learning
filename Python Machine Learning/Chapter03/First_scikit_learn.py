# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:13:35 2018

@author: 小周

"""

from sklearn import datasets
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import warnings


'''
Loading the Iris dataset from scikit-learn. 
Here, the third column represents the petal length, 
and the fourth column the petal width of the flower samples. 
The classes are already converted to integer labels 
where 0=Iris-Setosa, 1=Iris-Versicolor, 2=Iris-Virginica

'''

# 数据的导入和预处理
iris = datasets.load_iris()
X = iris.data[:, [2, 3]] # 获取iris数据集的第三列和第四列数据
y = iris.target

#print('Class labels:', np.unique(y))
# output:Class labels: [0 1 2]

# Splitting data into 70% training and 30% test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


# Standardizing the features:
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train) # Compute the mean and std to be used for later scaling
X_train_std = sc.transform(X_train) # Perform standardization by centering and scaling
X_test_std = sc.transform(X_test)

'''
=======================================
Training a perceptron via scikit-learn
=======================================

'''

from sklearn.linear_model import Perceptron
ppn = Perceptron(max_iter=40, eta0=0.01, random_state=0)
ppn.fit(X_train_std, y_train)
'''
Perceptron(alpha=0.0001, class_weight=None, eta0=0.1, fit_intercept=True,
      max_iter=40, n_jobs=1, penalty=None, random_state=0, shuffle=True,
      verbose=0, warm_start=False)
'''

y_pred = ppn.predict(X_test_std)

#print('Misclassified samples: %d' % (y_test != y_pred).sum())



#from sklearn.metrics import accuracy_score
#print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

def versiontuple(v):
    return tuple(map(int, (v.split("."))))

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
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
    
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.6,
                    c=cmap(idx),
                    edgecolor='black',
                    marker=markers[idx],
                    label=cl)
    # highlight test samples
    if test_idx:
        # plot all samples
        if not versiontuple(np.__version__) >= versiontuple('1.9.0'):
            X_test, y_test = X[list(test_idx), :], y[list(test_idx)]
            warnings.warn('Please update to NumPy 1.9.0 or newer')
        else:
            X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(X_test[:, 0],
                    X_test[:, 1],
                    c='',
                    alpha=1.0,
                    edgecolor='black',
                    linewidths=1,
                    marker='o',
                    s=55, label='test set')
'''
# Training a perceptron model using the standardized training data:
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

plot_decision_regions(X=X_combined_std, y=y_combined,
                      classifier=ppn, test_idx=range(105, 150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')

plt.tight_layout()
# plt.savefig('./figures/iris_perceptron_scikit.png', dpi=300)
plt.show()

'''














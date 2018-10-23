# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 14:55:54 2018

@author: 小周

"""

# K近邻算法
# K-nearest neighbors - a lazy learning algorithm

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import First_scikit_learn

#====================================================================
# 导入数据及预处理
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
X_combined = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))
#====================================================================


def knn():
    
    knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
    knn.fit(X_train_std, y_train)
    
    First_scikit_learn.plot_decision_regions(X_combined_std, y_combined,
                                             classifier=knn, test_idx=range(105, 150))
    plt.xlabel('petal length [standardized]')
    plt.ylabel('petal width [standardized]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    knn()








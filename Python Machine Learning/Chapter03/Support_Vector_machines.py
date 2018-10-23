# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 22:00:18 2018

@author: 小周

"""

'''
支持向量机
'''

# 3.1: 数据导入和预处理
import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
import matplotlib.pyplot as plt

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
y_combined = np.hstack((y_train, y_test))
#====================================================================



# 使用SVM的线性函数对iris的3,4列数据分类
def SVM_Linear_classsifier():
    svm = SVC(kernel='linear', C=1.0, random_state=0)
    svm.fit(X_train_std, y_train)

    #y_pred = svm.predict(X_test_std)
    #print('Misclassified samples: %d' % (y_test != y_pred).sum())
    
    First_scikit_learn.plot_decision_regions(X_combined_std, y_combined, classifier=svm, test_idx=range(105, 150))
    plt.xlabel('Petal length [standardized]')
    plt.ylabel('Petal width [standardized]')
    plt.legend(loc='upper left')
    plt.title('Support Vector Machine')
    plt.tight_layout()
    plt.show()

# Solving non-linear problems using a kernel SVM
def SVM_Nonlinear_classifier():
    np.random.seed(0)
    X_xor = np.random.randn(200, 2)
    y_xor = np.logical_xor(X_xor[:, 0] > 0, X_xor[:, 1] > 0)
    y_xor = np.where(y_xor, 1, -1)
    '''
    # 画出数据的散点图
    plt.scatter(X_xor[y_xor == 1,  0], X_xor[y_xor == 1,  1], c='b', marker='x', label='1')
    plt.scatter(X_xor[y_xor == -1, 0], X_xor[y_xor == -1, 1], c='r', marker='s', label='-1')
    plt.xlim([-3, 3])
    plt.ylim([-3, 3])
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
    '''
    svm = SVC(kernel='rbf', random_state=0, gamma=0.10, C=10.0)
    svm.fit(X_xor, y_xor)
    First_scikit_learn.plot_decision_regions(X_xor, y_xor, classifier=svm)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
# 使用SVM的rbf函数对iris数据集的3,4列分类
def SVM_rbf_classifier():
    
    #svm = SVC(kernel='rbf', random_state=0, gamma=0.2, C=1.0)
    svm = SVC(kernel='rbf', random_state=0, gamma=100.0, C=1.0)
    svm.fit(X_train_std, y_train)

    First_scikit_learn.plot_decision_regions(X_combined_std, y_combined, classifier=svm, test_idx=range(105, 150))
    plt.xlabel('petal length [standardized]')
    plt.ylabel('petal width [standardized]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    #SVM_Linear_classsifier()
    SVM_Nonlinear_classifier()
    #SVM_rbf_classifier()









# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 14:40:35 2018

@author: 小周

"""

# 随机森林
# Combining weak to strong learners via random forests

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
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

def random_forest():
    forest = RandomForestClassifier(criterion='entropy',
                                    n_estimators=10,
                                    random_state=1,
                                    n_jobs=2)
    forest.fit(X_train, y_train)
    First_scikit_learn.plot_decision_regions(X_combined, y_combined,
                                             classifier=forest, test_idx=range(105, 150))
    plt.xlabel('petal length [cm]')
    plt.ylabel('petal width [cm]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()





if __name__ == '__main__':
    random_forest()










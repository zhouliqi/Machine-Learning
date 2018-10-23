# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:40:54 2018

@author: 小周

"""

# 决策树
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier, export_graphviz
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


def gini(p):
    return p * (1 - p ) + (1 - p) * (1 - (1 - p))

def entropy(p):
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)

def error(p):
    return 1 - np.max([p, 1-p])

def test():
    x = np.arange(0.0, 1.0, 0.01)
    ent = [entropy(p) if p != 0 else None for p in x]
    sc_ent = [e * 0.5 if e else None for e in ent]
    err = [error(i) for i in x]
    
    fig = plt.figure()
    ax = plt.subplot(111)
    for i, lab, ls, c in zip([ent, sc_ent, gini(x), err],
                              ['Entropy', 'Entropy(scaled)',
                               'Gini Impurity', 'Misclassification error'],
                               ['-', '-', '--', '-.'],
                               ['black', 'lightgray', 'red', 'green', 'cyan']):
        line = ax.plot(x, i, label=lab, linestyle=ls, lw=2, color=c)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True, shadow=False)
    
    ax.axhline(y=0.5, linewidth=1, color='k', linestyle='--')
    ax.axhline(y=1, linewidth=1, color='k', linestyle='--')
    plt.ylim([0, 1.1])
    plt.xlabel('p(i=1)')
    plt.ylabel('Impurity Index')
    plt.tight_layout()
    plt.show()

# Building a decision tree
def Decision_Tree():
    tree = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
    tree.fit(X_train, y_train)
    
    X_combined = np.vstack((X_train, X_test))
    
    #export_graphviz(tree, out_file='tree.dot', feature_names=['petal length', 'petal width'])
    
    First_scikit_learn.plot_decision_regions(X_combined, y_combined, classifier=tree, test_idx=range(105, 150))
    plt.xlabel('petal length [cm]')
    plt.ylabel('petal width [cm]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

'''
def plot_Decision_image():
    from IPython.display import Image
    from IPython.display import display
    
    try:
        import pydotplus
        
        tree = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
        tree.fit(X_train, y_train)
        dot_data = export_graphviz(
                tree, 
                out_file=None,
                feature_names = ['petal length', 'petal width'],
                class_names = ['setosa', 'Versicolor', 'virginica'],
                filled = True,
                rounded=True)
        
        graph = pydotplus.graph_from_dot_data(dot_data)
        display(Image(graph.create_png()))
    except ImportError:
        print('pydotplus is not installed.')
'''


if __name__ == '__main__':
    #test()
    #Decision_Tree()
    plot_Decision_image()












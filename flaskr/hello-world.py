'''
Created on Jun 27, 2018

@author: zhaojialiang
'''
from sklearn import tree
"1 is smooth, 0 is bumpy"
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

#0 apple  1 origin
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print (clf.predict([[150, 0]]))
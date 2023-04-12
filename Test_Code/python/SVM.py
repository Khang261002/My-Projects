from sklearn import svm

X = [[0, 0], [2, 2], [3, 3]]
y = [0, 2, 3]
clf = svm.SVC()
clf.fit(X, y)
print(clf.predict([[1., 1.]]))

print(clf.support_vectors_)
print(clf.support_)
print(clf.n_support_)

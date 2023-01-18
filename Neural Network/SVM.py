from sklearn import svm

X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
print(clf.predict([[2., 2.]]))

print(clf.support_vectors_)
print(clf.support_)
print(clf.n_support_)

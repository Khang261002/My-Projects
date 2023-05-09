"""
mnist_svm
~~~~~~~~~

A classifier program for recognizing handwritten digits from the MNIST
data set, using an SVM classifier."""

#### Libraries
# My libraries
import hand_drawing
import mnist_loader

# Third-party libraries
import os
import joblib
from sklearn import svm

# main
def svm_baseline():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    if not os.path.isfile(os.path.join(__location__, "expanded_model.sav")):
        training_data, validation_data, test_data = mnist_loader.load_data()
        # train
        print("Training ...")
        clf = svm.SVC()
        clf.fit(training_data[0], training_data[1])
        # test
        print("Testing ...")
        predictions = [int(a) for a in clf.predict(test_data[0])]
        num_correct = sum(int(a == y) for a, y in zip(predictions, test_data[1]))
        print("Baseline classifier using an SVM.")
        print(str(num_correct) + " of " + str(len(test_data[1])) + " values correct.")
        if num_correct / len(test_data[1]) < 0.98:
            print("The clf is not good enough to save")
        else:
            print("The clf is quite good")
        joblib.dump(clf, os.path.join(__location__, "expanded_model.sav"))
    else:
        clf = joblib.load(os.path.join(__location__, "expanded_model.sav"))

    hand_drawing.check_drawing(clf)

if __name__ == "__main__":
    svm_baseline()

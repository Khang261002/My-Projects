"""
mnist_svm
~~~~~~~~~

A classifier program for recognizing handwritten digits from the MNIST
data set, using an SVM classifier."""

#### Libraries
# My libraries
import mnist_loader 

# Third-party libraries
import cv2
import numpy as np
from sklearn import svm

# mouse callback function
def line_drawing(event, x, y, flags, param):
    global pt1_x, pt1_y, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pt1_x, pt1_y = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (pt1_x, pt1_y), (x, y), color=(255, 255, 255), thickness=5)
            pt1_x, pt1_y = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (pt1_x, pt1_y), (x, y), color=(255, 255, 255), thickness=5)

# main
def svm_baseline():
    training_data, validation_data, test_data = mnist_loader.load_data()
    # train
    clf = svm.SVC()
    clf.fit(training_data[0], training_data[1])
    # test
    predictions = [int(a) for a in clf.predict(test_data[0])]
    num_correct = sum(int(a == y) for a, y in zip(predictions, test_data[1]))
    print("Baseline classifier using an SVM.")
    print(str(num_correct) + " of " + str(len(test_data[1])) + " values correct.")

    test = int(input("Do you want to try testing with your handwriting digit?\n\t1. Yes\n\t2. No\n"))
    while test == 1:
        global drawing, mode, img
        drawing = False
        mode = True

        img = np.zeros((128, 128), np.uint8)

        cv2.namedWindow("Write a Digit")
        cv2.setMouseCallback("Write a Digit", line_drawing)

        while True:
            cv2.imshow("Write a Digit", img)
            key = cv2.waitKey(1)
            if key != -1:
                break

        img = cv2.resize(img, (28, 28))
        img = np.multiply(img, 1/255)
        img = np.reshape(img, (1, 784))
        print("The digit is %d" % int(clf.predict(img)))

        cv2.destroyAllWindows()
        test = int(input("Test again?\n\t1. Yes\n\t2. No\n"))

    cv2.destroyAllWindows()

if __name__ == "__main__":
    svm_baseline()

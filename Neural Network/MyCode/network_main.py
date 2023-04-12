#### Libraries
# My libraries
import mnist_loader
import network

### Third-party Libraries
import cv2
import numpy as np

# mouse callback function
def line_drawing(event, x, y, flags, param):
    global pt1_x, pt1_y, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pt1_x, pt1_y = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (pt1_x, pt1_y), (x, y), color=(255, 255, 255), thickness=15)
            pt1_x, pt1_y = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (pt1_x, pt1_y), (x, y), color=(255, 255, 255), thickness=15)

def check_drawing():
    test = int(input("Do you want to try testing with your handwriting digit?\n\t1. Yes\n\t2. No\n"))
    while test == 1:
        global drawing, mode, img
        drawing = False
        mode = True

        img = np.zeros((256, 256), np.uint8)

        cv2.namedWindow("Write a Digit")
        cv2.setMouseCallback("Write a Digit", line_drawing)

        while True:
            cv2.imshow("Write a Digit", img)
            key = cv2.waitKey(1)
            if key != -1:
                break
        
        # delete all lines of pixels around which have no drawing
        img = img[~np.all(img == 0, axis=1), :]
        img = img[:, ~np.all(img == 0, axis=0)]
        rows, cols = img.shape

        expected_height = round(rows * 1.5)
        for i in range(expected_height - rows):
            if i % 2 == 0:
                img = np.r_[[np.zeros(cols)], img]
            else:
                img = np.r_[img, [np.zeros(cols)]]

        rows = expected_height
        if rows > cols:
            for i in range(rows - cols):
                if i % 2 == 0:
                    img = np.c_[np.zeros(rows), img]
                else:
                    img = np.c_[img, np.zeros(rows)]
        if rows < cols:
            for i in range(cols - rows):
                if i % 2 == 0:
                    img = np.r_[[np.zeros(cols)], img]
                else:
                    img = np.r_[img, [np.zeros(cols)]]
        
        img = cv2.resize(img, (28, 28))
        img = np.multiply(img, 1/255)
        img = np.reshape(img, (784, 1))
        print("The digit is %d" % net.directly_test(img))

        cv2.destroyAllWindows()
        test = int(input("Test again?\n\t1. Yes\n\t2. No\n"))

    cv2.destroyAllWindows()

if __name__ == "__main__":
    training_data, validation_data, test_data = \
        mnist_loader.load_data_wrapper()
    net = network.Network([784, 30, 10])
    net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
    check_drawing()

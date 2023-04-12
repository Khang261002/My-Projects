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
            cv2.line(img, (pt1_x, pt1_y), (x, y), color=(255, 255, 255), thickness=5)
            pt1_x, pt1_y = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (pt1_x, pt1_y), (x, y), color=(255, 255, 255), thickness=5)

# main function
if __name__ == "__main__":
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
    
    img = img[~np.all(img == 0, axis=1), :]
    img = img[:, ~np.all(img == 0, axis=0)]
    rows, cols = img.shape
    if rows > cols:
        for i in range(rows - cols):
            if i % 2 == 0:
                img = np.c_[np.zeros(rows), img]
            else:
                img = np.c_[img, np.zeros(rows)]
    if rows < cols:
        for i in range(cols - rows):
            if i % 2 == 0:
                img = np.r_[np.zeros(cols), img]
            else:
                img = np.r_[img, np.zeros(cols)]

    img = cv2.resize(img, (28, 28))
    img = np.multiply(img, 1/255)
    img = np.reshape(img, (784, 1))

    cv2.destroyAllWindows()
    print("Complete!")

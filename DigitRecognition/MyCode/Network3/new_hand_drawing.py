import numpy as np
import pandas as pd
import new_network3
import cv2

# mouse callback function
def line_drawing(event, x, y, flags, param):
    global pt1_x, pt1_y, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pt1_x, pt1_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (pt1_x, pt1_y), (x, y), color=(255, 255, 255), thickness=12)
            pt1_x, pt1_y = x, y
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (pt1_x, pt1_y), (x, y), color=(255, 255, 255), thickness=12)

def compare_Contours(cnt1, cnt2):
    return (((cnt1[0] < cnt2[0]) and (cnt1[1] < cnt2[1] + cnt2[3])) 
            or ((cnt1[0] == cnt2[0]) and (cnt1[1] < cnt2[1])) 
            or (cnt1[1] + cnt1[3] < cnt2[1]))

def merge_Sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
 
        # Sorting the first half
        merge_Sort(L)
        # Sorting the second half
        merge_Sort(R)
 
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if compare_Contours(L[i], R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def check_drawing(model):
    test = int(input("Do you want to try testing with your handwriting digit?\n\t1. Yes\n\t2. No\n"))
    while test == 1:
        global drawing, mode, img
        drawing = False
        mode = True

        img = np.zeros((512, 512), np.uint8)

        cv2.namedWindow("Write a Digit")
        cv2.setMouseCallback("Write a Digit", line_drawing)     # Draw line using mouse

        while True:
            cv2.imshow("Write a Digit", img)
            key = cv2.waitKey(1)
            if key != -1:
                break
        
        # Use OpenCV to find all the digits. Access the link below for more information.
        # https://docs.opencv.org/3.1.0/d9/d8b/tutorial_py_contours_hierarchy.html
        contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        pos_list = []
        img_list = []

        for i in range(0, len(contours)):
            if hierarchy[0, i, 3] == -1:
                pos_list.append(contours[i])

        pos_list = [cv2.boundingRect(i) for i in pos_list]
        merge_Sort(pos_list)

        for i in range(0, len(pos_list)):
            x, y, w, h = pos_list[i]
            img_list.append(img[y : y + h + 1, x : x + w + 1])

        # while True:
        #     cv2.imshow("Write a Digit", img)
        #     for cnt in pos_list:
        #         x, y, w, h = cnt
        #         cv2.rectangle(img, (x, y), (x + w, y + h), (255), 2)
        #     key = cv2.waitKey(1)
        #     if key != -1:
        #         break
        
        for img_number in img_list:
            rows, cols = img_number.shape

            expected_height = round(rows * 1.5)
            for i in range(expected_height - rows):
                if i % 2 == 0:
                    img_number = np.r_[[np.zeros(cols)], img_number]
                else:
                    img_number = np.r_[img_number, [np.zeros(cols)]]
            
            rows = expected_height
            if rows > cols:
                for i in range(rows - cols):
                    if i % 2 == 0:
                        img_number = np.c_[np.zeros(rows), img_number]
                    else:
                        img_number = np.c_[img_number, np.zeros(rows)]
            if rows < cols:
                for i in range(cols - rows):
                    if i % 2 == 0:
                        img_number = np.r_[[np.zeros(cols)], img_number]
                    else:
                        img_number = np.r_[img_number, [np.zeros(cols)]]
            
            img_number = cv2.resize(img_number, (28, 28))
            img_number = np.multiply(img_number, 1/255)
            
            if type(model) == new_network3.Network:
                img_number = np.reshape(img_number, (1, 784))
                print("%d" % model.predict(img_number), end="")
        
        cv2.destroyAllWindows()
        test = int(input("\nTest again?\n\t1. Yes\n\t2. No\n"))

    cv2.destroyAllWindows()
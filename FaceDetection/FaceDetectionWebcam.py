import cv2
import operator

def rainbow_autochange():
    global rgb, index, increase
    if (rgb[index] == 0 and increase == False) or (rgb[index] == 255 and increase == True):
        increase = operator.not_(increase)
        index -= 1
        if index == -1:
            index = 2
    rgb[index] -= 5*((-1)**(int(increase)))

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
rgb = [255, 0, 0]
t = 1
increase = True
idx = 0

while True:
    successful_frame_read, frame = webcam.read()
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (rgb[2], rgb[1], rgb[0]), 5)
    rainbow_autochange()
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)
    #print(key)
    if key == 49 and idx != 0:
        webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        idx = 0
    elif key == 50 and idx != 1:
        webcam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        idx = 1
    elif key != -1 and key != 49 and key != 50:
        break
# Release the webcam
webcam.release()
cv2.destroyAllWindows()
print('#----------------------------#\n\tCode Completed')

'''
r = 255
g = b = 0
def rgb_autochange():
    global r, g, b, increase, index
    if index == 1:
        if increase:
            if g < 255:
                g += 5
            else:
                increase = False
                index = 2
                r -= 5
        else:
            if g > 0:
                g -= 5
            else:
                increase = True
                index = 2
                r += 5
    elif index == 2:
        if increase:
            if r < 255:
                r += 5
            else:
                increase = False
                index = 3
                b -= 5
        else:
            if r > 0:
                r -= 5
            else:
                increase = True
                index = 3
                b += 5
    else:
        if increase:
            if b < 255:
                b += 5
            else:
                increase = False
                index = 1
                g -= 5
        else:
            if b > 0:
                b -= 5
            else:
                increase = True
                index = 1
                g += 5

def rainbow_autochange():
    global rgb, index, increase
    if increase:
        if rgb[index] < 255:
            rgb[index] += 5
        else:
            increase = False
            index -= 1
            if index == -1:
                index = 2
            rgb[index] -= 5
    else:
        if rgb[index] > 0:
            rgb[index] -= 5
        else:
            increase = True
            index -= 1
            if index == -1:
                index = 2
            rgb[index] += 5
'''
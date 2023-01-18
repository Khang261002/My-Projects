import cv2
from random import randrange

# STEP 1: Get a scrap-load of faces
# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Choose an image to detect faces in
img = cv2.imread('Random.png')

# STEP 2: Convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# STEP 3: Train the algorithm to detect faces
#Detect face
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# x and y are coordinates of the top left point. w is the width and h is the height
for (x, y, w, h) in face_coordinates:  
    cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 5) # First coordinates, second coordinates, BGR color, thickness

# Show the image and immediately close it
cv2.imshow('Face Detector', img)
# Wait until you press any key
cv2.waitKey()
print('#----------------------------#\n\tCode Completed')

import face_recognition
import cv2
import numpy as np

#从图片中识别人脸  并进行标注
frame = cv2.imread('D:/test/3face.jpg')

frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)

# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses) 
rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
face_locations = face_recognition.face_locations(rgb_frame)

for face_location in face_locations:
    # Draw a box around the face
    top = face_location[0]
    right = face_location[1]
    bottom = face_location[2]
    left = face_location[3]
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

cv2.imshow('img', frame)
cv2.imwrite('3faceout.jpg', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
import matplotlib as plt
import face_recognition

cap = cv2.VideoCapture('D:/test/video.mp4')

videoWrite = cv2.VideoWriter('outvideo.avi', cv2.VideoWriter_fourcc(*'XVID'),20,(426,240))

while True:
    ret, frame = cap.read()
    print(frame.shape)
    
    if frame is None:
        break
    
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses) 
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame,model='hog')
    for face_location in face_locations:
        # Draw a box around the face
        top = face_location[0]
        right = face_location[1]
        bottom = face_location[2]
        left = face_location[3]
        print(face_location)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    videoWrite.write(frame)
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
    

cap.release()
videoWrite.release()
cv2.destroyAllWindows()




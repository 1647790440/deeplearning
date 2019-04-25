import face_recognition
import cv2
import numpy as np

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) 

# Initialize some variables
face_locations = []

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    #change into RGB
    feame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    # Resize frame of video to 1/4 size for faster face detection processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    #缩小尺寸能十分有效的减少运算量，指数级别的减少  这个例子就减少为原来的1/16
    #但是缺点也很明显，识别度明显降低，特别是当人离摄像头比较远的时候

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(small_frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
    
    out.write(frame)
    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
out.release()
cv2.destroyAllWindows()
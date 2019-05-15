import numpy as np
import face_recognition
import json

def faceencode(inputpath):
    img = face_recognition.load_image_file(inputpath)
    imgencode = face_recognition.face_encodings(img)[0]
    bytes_imgencode = imgencode.tostring()
    return bytes_imgencode

def facedecode(bytes_imgencode)
    imgencode = np.frombuffer(bytes_imgencode,dtype=np.float64)
    return imgencode



def facerecognition(inputimgpath,ids):                               #未完成版
    for id in ids:
        imgencode.append(facedecode(id))                             #已知图片编码
    unknown_image = face_recognition.load_image_file(inputimgpath)   #上传的图片的路径  
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(imgencode, face_encoding)
        face_distances = face_recognition.face_distance(imgencode, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            attendid = ids[best_match_index]
            outputids.append(attendid)
    return outputids

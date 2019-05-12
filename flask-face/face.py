import numpy as np
import face_recognition
import json
import os
#import cv2
from PIL import Image, ImageDraw, ImageFont

#要写成函数的模式

basedir = os.path.abspath(os.path.dirname(__file__))

path = basedir + '/static/单独/'
 
# 读取path文件夹下所有文件的名字
imagelist = os.listdir(path)
imgencode = []
names = []
outputnames = {}
dict = {} 
for imgname in imagelist:
    if(imgname.endswith(".jpg")):
        #image = cv2.imdecode(np.fromfile(path+imgname,dtype=np.uint8),-1)
        names.append(imgname[:-4])
        cur = face_recognition.load_image_file(path+imgname)
        imgencode.append(face_recognition.face_encodings(cur)[0])
#这边可以先对上传的图片进行缩放


def facerecognition(inputpath):
    id = 1
    global outputnames,dict
    unknown_image = face_recognition.load_image_file(inputpath)   #上传的图片的路径
    img = Image.open(inputpath)                                     #上传的图片的路径
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(imgencode, face_encoding)
        name = "Unknown person"
        face_distances = face_recognition.face_distance(imgencode, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = names[best_match_index]
        dict = {'id':id,'name':name}
        outputnames[id-1] = dict
        id = id + 1
        draw = ImageDraw.Draw(img) 
        draw.line((left,top,left,bottom),'red')
        draw.line((right,top,right,bottom),'red')
        draw.line((left,top,right,top),'red')
        draw.line((left,bottom,right,bottom),'red')
        font = ImageFont.truetype("simhei.ttf" ,int((right-left)/4), encoding="utf-8") # 参数1：字体文件路径，参数2：字体大小
        draw.text((left,top-int((right-left)/4)),name, (255, 255, 255), font=font) # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
    img.save(basedir + '/static/识别ed/' + '识别.jpg')
    return outputnames
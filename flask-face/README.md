## 目标：

实现在网页前端上传图片，后端接收完成人脸识别，再将识别数据和图片返回给前端。

## 流程：

1.flask作为web框架，实现前后端的数据联通。

2.前端提供文件上传功能（上传所要识别的图片）和结果展示功能（展示识别成功的人脸数据和已经标识好人脸信息的图片）。

2.后端将要实现的功能打包成一个函数接口供前端调用，以要识别的图片为输入，识别结果为输出。函数功能基于face_recognition库实现人脸识别。

## 运行效果图：

图片的上传：

![](https://github.com/1647790440/deeplearning/blob/master/flask-face/%E6%95%88%E6%9E%9C%E5%9B%BE/%E5%9B%BE%E7%89%87%E4%B8%8A%E4%BC%A0.png?raw=true)

数据的返回：

![](https://github.com/1647790440/deeplearning/blob/master/flask-face/%E6%95%88%E6%9E%9C%E5%9B%BE/%E5%9B%BE%E7%89%87%E8%BF%94%E5%9B%9E1.jpg?raw=true)

![](https://github.com/1647790440/deeplearning/blob/master/flask-face/%E6%95%88%E6%9E%9C%E5%9B%BE/%E5%9B%BE%E7%89%87%E8%BF%94%E5%9B%9E2.jpg?raw=true)

## 还可以改进的地方：

1.由于以前没做过html和jacascript，前端届面太简陋。

2.文件上传和再后端的保存也只是最基本的功能，只能实现一张图片的处理。没有安全保障措施，如上传文件的格式控制（防止上传的文件不是图片而导致后端服务崩溃），保存方面也存在不足，如上传文件名重复，就直接覆盖掉了。

3.后端单独的人脸信息实在服务器启动时才开始加载和编码信息的，因此在启动的时候需要挺长的一段时间才能完成启动。应先对单独的人脸信息进行处理，将识别编码的数据储存（数据库）起来直接使用，而不是每次启动再重新识别编码一次。

4.还存在技术难题，成功率，速度，都有待改进。

## 代码：

前端代码：

上传页面：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/upload" method="post" enctype="multipart/form-data">
    <p>
        <input type="file" name="file">
        <input type =submit value="upload">
    </p>
</form>
</body>
</html>
```

识别之后返回页面：

```html
<!DOCTYPE html>
<html lang="en"> 
<body>
	<script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.js"></script>
		<script>
		var data;
        $.ajax({
			url: "test_post",
			data:data,
			type: "post",
			dataType: "json",
			success: function (data) {
				document.write("<p>数据结果展示：</p>");
				document.write(data);
				document.write("<p>图片结果展示：</p>");
				document.write("<img src='../static/识别ed/识别.jpg' width='720' height='480'>");
			}
        }) 
		</script>
</body>
 
</html>
```

后端代码：

flask：

```python
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response, redirect, url_for
from flask import jsonify
from werkzeug.utils import secure_filename
from os import path
import json
import face   #打包的face函数

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
@app.route('/index')
def home():
    return render_template(
        'index.html'
    )

message = 'hello world'

@app.route("/upload",methods=['GET','POST'])
def upload():
    global message
    if request.method=='POST':
        f = request.files["file"]  #读取上传图片，并交给识别函数
        base_path = path.abspath(path.dirname(__file__))
        upload_path = path.join(base_path,'static/uploads/')
        file_name = upload_path + secure_filename(f.filename)
        print(file_name)
        f.save(file_name)
        message = face.facerecognition(file_name)
        #调用face.py文件中的facerecognition函数完成图片的识别
    return render_template('return.html')#返回完成界面

@app.route('/test_post',methods=['GET','POST'])
def test_post():
    global message
    if request.method=='POST':
        message =json.dumps(message,ensure_ascii=False,indent = 4)
        #print(message)
    return jsonify(message)  #向前端返回数据结果

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

```

face_recognition:

```python
#face函数，在主文件中引入
import numpy as np
import face_recognition
import json
import os
from PIL import Image, ImageDraw, ImageFont

imgencode = []
names = []
outputnames = {}
dict = {} 

basedir = os.path.abspath(os.path.dirname(__file__))
path = basedir + '/static/单独/'
 
#读取path文件夹下所有文件的名字
#对'/static/单独/'目录下的所有图片进行读取
imagelist = os.listdir(path)
for imgname in imagelist:
    if(imgname.endswith(".jpg")):
        names.append(imgname[:-4])  #得到图片所对应的名字，去掉文件名后边的“.jpg”
        cur = face_recognition.load_image_file(path+imgname) #读取图片
        imgencode.append(face_recognition.face_encodings(cur)[0]) #编码，然后放进列表

def facerecognition(inputpath):   #定义功能函数
    id = 1
    global outputnames,dict
    unknown_image = face_recognition.load_image_file(inputpath) #inputpath上传的图片的路径
    img = Image.open(inputpath)                                
    
    #人脸识别
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
        #用PIL对人脸进行标识（由于cv2不支持中文，因此选用PIL，比较方便）
        draw = ImageDraw.Draw(img) 
        draw.line((left,top,left,bottom),'red')
        draw.line((right,top,right,bottom),'red')
        draw.line((left,top,right,top),'red')
        draw.line((left,bottom,right,bottom),'red')
        font = ImageFont.truetype("simhei.ttf" ,int((right-left)/4), encoding="utf-8")
        draw.text((left,top-int((right-left)/4)),name, (255, 255, 255), font=font)
        
    img.save(basedir + '/static/识别ed/' + '识别.jpg') #保存识别之后的图片
    return outputnames
```

## 参考：

<https://blog.csdn.net/dcrmg/article/details/81987808>

<https://blog.csdn.net/u010197393/article/details/83503202>

<https://www.cnblogs.com/flyhigh1860/p/3896111.html>
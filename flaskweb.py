from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask import request
from flask import render_template
import face
 
app = Flask(__name__)
wsgi_app = app.wsgi_app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/flaskweb'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
 
class User(db.Model):
    # 定义表名
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    phone = db.Column(db.String(15))
    photo = db.Column(db.String(100))
    faceenode = db.Column(db.LargeBinary(length=2048))
    profilephoto = db.Column(db.String(100))
    joinedclasses = db.Column(db.String(1000))
    establishedclasses = db.Column(db.String(1000))
    bytes_imgencode = db.Column(db.LargeBinary)
 
class Calss(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    classname = db.Column(db.String(20), unique=True)
    invitationcode = db.Column(db.String(20))
    numberofstudents = db.Column(db.Integer)
    idofstudents = db.Column(db.String(2000))
    isallowedtojoin = db.Column(db.Integer)

    
    
@app.route("/register",methods=['GET','POST'])   #用户注册
def register():
    
    #从前端获得username password phone photo
    
    data = request.get_data()
    u = None
    u = User.query.filter_by(phone=data['phone']).all()
    if u == None:
        #该手机号可以使用
        b_img = face.faceencode(data['photo']) #对图片进行编码
        u = User(username=data[username],password=data[password],phone=data[phone],photo=data[photo],bytes_imgencode=b_img)    #其他项默认为空？
        db.session.add_all(u)
        db.session.commit()
        #添加到数据库
        return 1 #注册成功！
    else:
        return 0 #该手机号已经被注册！

@app.router("/signin",methods=['GET','POST'])    #用户登入
def signin():
    
    #从前端获得phone password
    
    data = request.get_data()
    u = None
    u = User.query.filter_by(phone=data['phone']).all()
    if u == None:
        return 0         #用户名不存在！
    else:
        if u.password == data['password'] :
            return 1     #正确！
        else:
            return 0     #密码错误！
    #前端如果接受到0表示用户名或在密码错误，请从新输入
    #如果接收到1，表示用户名的密码匹配，可以接着发送请求usermessage，即下一个⬇
        
@qpp.router("/usermessage",methods=['GET','POST'])   #返回个人信息  未完成  不足道要返回哪些信息，要什么格式
def usermessage():
    
    #从前端获得 (已经确认正确的)   登入手机号 phone
    
    data = request.get_data()
    u = User.query.filter_by(phone=data['phone']).all()
    return message  #返回个人信息，格式还未完整，message还未确定

@app.router("/classmessage",methods=['GET','POST'])  #返回班级信息  同上 未完成  不足道要返回哪些信息，要什么格式
def classmessage():
    
    #从前端获得 班级id
    
    data = request.get_data()
    c = Class.query.get(data['id'])
    return message   #返回班级信息，格式还未完整，message还未确定
    
    
    
@app.router("/createclass",methods=['GET','POST'])  #创建班级
def createclass():
    
    #从前端获取classname 创建者id 随即生成的invitationcode，班级名classname 
    
    #这边还需要一个检测invitationcode是否合法的函数，邀请码要唯一的,放在邀请码生成函数,由前端完成？
    
    data = request.get_data()
    c = Class(classname = data['classname'],invitationcode = data['invitationcode'],numberofstudents = 0，isallowedtojoin = 1)
    db.session.add_all(c)
    db.session.commit()  #更新到数据库
    
    #创建人表单中加入该班级id
    
    c = Class.query.filter_by(invitationcode=data['incitationcode']).all()
    u = User.query.get(data['id'])
    if u.establishedclasses != None :
        u.establishedclasses = u.establishedclasses + ',' + string(c.id)     #可能需要中间变量
    else:
        u.establishedclasses = string(c.id)
    db.session.commit()  #更新到数据库
    
    return 1 #创建成功！

@app.router("/joinclass",methods=['GET','POST'])   #加入班级
def joinclass():
    #在对应班级的表但上填入学生id
    #在学生的表但上填入班级id
    #班级人数+1
    
    #从前端获得   班级邀请码incitationcode，学生id
    
    #这边还需要检测该班级是否允许加入 isallowtijoin == 1 ?  未完成

    data = request.get_data()
    c = None
    c = User.query.filter_by(invitationcode=data['invitationcode']).all()
    if c == None:
        return 0       #没找到对应班级，则邀请码invitationcode错误，返回0
    else:
        if c.isallowtojoin == 1 :
            u = User.query.get(data['id'])
            c = Class.query.filter_by(invitationcode=data['incitationcode']).all()
            if u.joinedclasses != None:
                u.joinedclasses = u.joinedclasses + ',' +string(c.id)   #可能需要引入一个中间变量，还未实验
            else:
                u.joinedclasses = string(c.id)
            db.session.commit()
            #更新到数据库
            c.numberofstudents = c.numberofstudents + 1
            db.session.commit()
            #更新到数据库
            if c.idofstudents != None:
                c.idofstudents = c.idofstudents + ',' + string(u.id)
            else:
                c.idofstudents = string(u.id)
            db.session.commit()
            #更新到数据库
            return 1    #成功加入班级
        else:
            return 0    #该班级不允许被加入
    #返回0有两个可能 invitationcode错误或者 该班级不允许被加入
    #返回1就是加入成功
    
@qpp.router("/changeclassright",methods=['GET','POST']) #修改班级权限，是否可以加入
def changeclassright():
    
    #从前端得到  班级id 
    
    data = request.get_data()
    c = Class.query.get(data['id'])
    if c.isallowtohoin == 1 :
        c.isallowtojoin = 0
    else:
        c.isallowtojoin = 1
    
    return 1  #修改成功！

@app.router("/rollcall",methods=['GET','POST'])   #点名    返回信息格式  图片保存 命名等  都未完成
def rollcall():
    
    #从前端获取要点名的照片photo（路径），班级id
    
    data = request.get_data()
    imgencode = []
    c = Class.get(data['id'])
    for i in c.idofstudents.split(str=','):
        i = int(i)
        u = User.query.filter_by(id = i)
        imgencode.append(face.facedecode(u.bytes_imgencode))   #调用识别函数   函数在  face.py   文件中
    output = facerecognition(data[photo],imgencode)
    #返回识别信息
    return jsonify(output)            #生成图片，还未完成


#布置作业等逻辑性复杂的功能暂时不实现


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    db.drop_all()
    db.create_all()
    app.run(debug=False)
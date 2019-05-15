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
 
class Calss(db.Model):
    __tablename__ = 'class'
    id = db.Column(db.Integer, primary_key=True)
    classname = db.Column(db.String(20), unique=True)
    invitationcode = db.Column(db.String(20))
    numberofstudents = db.Column(db.Integer)
    idofstudents = db.Column(db.String(2000))
    idofhomework = db.Column(db.String(2000))
    isallowedtojoin = db.Column(db.Integer)
    absentstudents = db.Column(db.Text)
    absentrate = db.Column(db.Float)
    
class Homework(db.Model):
    __tablename__ = 'homework'
    id = db.Column(db.Integer, primary_key=True)
    assignment = db.Column(db.Text)
    classid = db.Column(db.Integer)
    releasetime = db.Column(db.DateTime)
    
    
@app.route("/register",methods=['GET','POST'])   #用户注册
def register():
    return 0

@app.router("/signin",methods=['GET','POST'])    #用户登入
def signin():
    return 0

@app.router("/createclass",methods=['GET','POST'])  #创建班级
def createclass():
    return 0

@app.router("/joinclass",methods=['GET','POST'])   #加入班级
def joinclass():
    return 0

@app.router("/rollcall",methods=['GET','POST'])   #点名
def rollcall():
    return 0

@qpp.router("/homework",methods=['GET','POST'])   #布置作业
def homework():
    return 0

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    db.drop_all()
    db.create_all()
    app.run(debug=False)
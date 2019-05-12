"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import request
from flask import render_template
from flask import make_response, redirect, url_for
from flask import jsonify
from werkzeug.utils import secure_filename
from os import path
import json
import face

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
@app.route('/index')
def home():
    """Renders the home page."""
    return render_template(
        'index.html'
    )

message = 'hello world'

@app.route("/upload",methods=['GET','POST'])
def upload():
    global message
    if request.method=='POST':
        f = request.files["file"]
        base_path = path.abspath(path.dirname(__file__))
        upload_path = path.join(base_path,'static/uploads/')
        file_name = upload_path + secure_filename(f.filename)
        print(file_name)
        f.save(file_name)
        message = face.facerecognition(file_name)
    return render_template('return.html')

@app.route('/test_post',methods=['GET','POST'])
def test_post():
    global message
    if request.method=='POST':
        message =json.dumps(message,ensure_ascii=False,indent = 4)
        print(message)
    return jsonify(message)

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

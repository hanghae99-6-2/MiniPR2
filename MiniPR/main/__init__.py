from flask import Flask , render_template , request , jsonify , session, redirect, url_for 
from pymongo import MongoClient
import certifi
import requests
from bs4 import BeautifulSoup
# 회원가입/로그인
import jwt
import hashlib
import json

#db 파일 불러오기
with open('main/config.json', 'r') as f:
    config = json.load(f)
secret_ID = config['DEFAULT']['ADMIN_NAME']
secret_key = config['DEFAULT']['SECRET_KEY']

#db 연결

ca = certifi.where()
client = MongoClient(f'mongodb+srv://{secret_ID}:{secret_key}@cluster0.ypa9i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.MiniPR2


SECRET_KEY = 'SPARTA'

#__init__.py 파일에선 app 객체를 선언하고 각종 모듈, 데이터베이스, 블루프린트 등 값을 설정한다

from . import main       #from . import main : main.py의 내용을 호출하겠다.
from . import login    
from . import sign_up   
from . import community 


app = Flask(__name__)

app.register_blueprint(community.blueprint)
app.register_blueprint(main.blueprint) # (main.blueprint) main.py에서 사용할 blueprint객체를 blueprint로 설정할거야
app.register_blueprint(login.blueprint) 
app.register_blueprint(sign_up.blueprint)


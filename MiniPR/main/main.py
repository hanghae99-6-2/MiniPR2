#main에 선언된 모든 값을 가져온다
from main import *
from flask import Blueprint

#객체 = Blueprint("name" , __name__ , url_prefix="") : (이름, 모듈명, URL 프리픽스 값)
#이름은 url_for함수에서 사용되며 , 모듈명은 init.py에서 선언한 모듈을 뜻함 , url_prefix="주소"의 주소에는 브라우져에서 선언될 url을 입력한다

blueprint = Blueprint("main" , __name__ , url_prefix="/main")


@blueprint.route("/")                                                                                     #route:url을 함수와 연결하는데 사용
def main_template():                                                                                      #└ "/~"는 main_template함수와 연결되어 http://localhost:5000/~ 를 방문하면 return값이 불러와짐
    return render_template("main.html")                                                                   #main.html 불러옴, return:결과값을 돌려주는 명령어


@blueprint.route("/sedan")
def sedan_template():
    return render_template("sedan.html")

@blueprint.route("/hatchback")
def hatchback_template():
    return render_template("hatchback.html")

@blueprint.route("/suvv")
def suvv_template():
    return render_template("suvv.html")

@blueprint.route("/coupe")
def coupe_template():
    return render_template("coupe.html")

@blueprint.route("/truck")
def truck_template():
    return render_template("truck.html")
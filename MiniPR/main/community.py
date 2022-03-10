from main import * #from main import * : main에 선언된 모든 값을 가져온다 , __init__ file에 선언된 라이브러리를 가져와 사용할 수 있음.
from flask import Blueprint
import datetime

#객체 = Blueprint("name" , __name__ , url_prefix="") : (이름, 모듈명, URL 프리픽스 값)
#이름은 url_for함수에서 사용되며 , 모듈명은 init.py에서 선언한 모듈을 뜻함 , url_prefix="주소"의 주소에는 브라우져에서 선언될 url을 입력한다 

blueprint = Blueprint("community" , __name__ , url_prefix="/community")

@blueprint.route("/") #<- 데코레이터
def community_template():
    cars = list(db.cars.find({},{'_id':False}))

    return render_template("community.html" , car = cars)

@blueprint.route("/boltEV") #<- 데코레이터
def community1_template():
    cars = list(db.cars.find({},{'_id':False}))
    
    return render_template("community1.html" , car = cars)

@blueprint.route("/spark") #<- 데코레이터
def community2_template():
    cars = list(db.cars.find({},{'_id':False}))


    return render_template("community2.html" , car = cars)

@blueprint.route("/treverse") #<- 데코레이터
def community3_template():
    cars = list(db.cars.find({},{'_id':False}))

    return render_template("community3.html" , car = cars)

@blueprint.route("/bolteuv") #<- 데코레이터
def community4_template():
    cars = list(db.cars.find({},{'_id':False}))
    
    return render_template("community4.html" , car = cars)

@blueprint.route("/trax") #<- 데코레이터
def community5_template():
    cars = list(db.cars.find({},{'_id':False}))
    
    return render_template("community5.html" , car = cars)

@blueprint.route("/treble") #<- 데코레이터
def community6_template():
    cars = list(db.cars.find({},{'_id':False}))
    
    return render_template("community6.html" , car = cars)

@blueprint.route("/camaro") #<- 데코레이터
def community7_template():
    cars = list(db.cars.find({},{'_id':False}))
    
    return render_template("community7.html" , car = cars)

@blueprint.route("/colorado") #<- 데코레이터
def community8_template():
    cars = list(db.cars.find({},{'_id':False}))
    
    return render_template("community8.html" , car = cars)





@blueprint.route("/comment_post" , methods = ["POST"])
def comment_post():
        SECRET_KEY = 'CAR'
        token_receive = request.cookies.get('token') #쿠키에서 토큰을 받아올 것
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256']) #로그인한 페이지이기 때문에 jwt에 token정보를 읽어옴
        
        user_info = db.users.find_one({"username": payload["id"]}) #페이로드와 동일한 데이터
         

        comment_receive = request.form['comment_give']#클라이언트에서 받은 유저의 input을 받아올 것
        day = datetime.datetime.now()  #데이터가 들어가는 실시간 시간 저장
        now = day.strftime('%Y-%m-%d')
        

        
        comment = comment_receive #유저의 input 값
        index = request.form['index_give'] # 메인의 이름과 같은 데이터를 객체로 받아왔다 -> 같은 데이터에 업데이트 하는 형식

        doc = {
            "user_name" : user_info['username'] , 
            "user_email" : user_info['email'],
            "now" : now ,
            "comment" : comment
            }
        
        db.cars.update_one({"carname" : index} , {'$push':{'comment' : doc}})

        return ({"msg" : "댓글 저장 완료!"})

# @blueprint.route("/post_card" , methods = ["GET"]) #<- 데코레이터
# def posting_card():
#     cars = list(db.cars.find({},{'_id':False}))
#     return jsonify({'card': cars})

@blueprint.route("/comment_delete" , methods = ["POST"]) #<- 데코레이터
def posting_card():
    cars = list(db.cars.find({},{'_id':False}))

    return jsonify({'card': cars})



 #     #1. GET : DB에서 Data를 찾아 Client에서 호출할 수 있게 return값을 할당
 # 2. POST : Client에서 Data를 받아 DB에 저장
 # - Client
 #     1. GET : Server에서 Data를 받아 posting
 #     2. POST : 사용자의 Input값을 data형식 지정 후 Server에 전송
from main import * #from main import * : main에 선언된 모든 값을 가져온다 , __init__ file에 선언된 라이브러리를 가져와 사용할 수 있음.
from flask import Blueprint

#객체 = Blueprint("name" , __name__ , url_prefix="") : (이름, 모듈명, URL 프리픽스 값)
#이름은 url_for함수에서 사용되며 , 모듈명은 init.py에서 선언한 모듈을 뜻함 , url_prefix="주소"의 주소에는 브라우져에서 선언될 url을 입력한다 

blueprint = Blueprint("sign_up" , __name__ , url_prefix="/sign_up")

@blueprint.route("/") #<- 데코레이터
def sign_up_template():
    return render_template("sign_up.html")

@blueprint.route('/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']                                        # 유저 이름을 받고
    password_receive = request.form['password_give']                                        # 패스워드를 받고
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()            # 해쉬 함수를 걸어준다
    email_receive = request.form['email_give']
    doc = {
        "username": username_receive,                               # 아이디
        "password": password_hash,                                  # 비밀번호
        "profile_name": username_receive,                           # 프로필 이름 기본값은 아이디
        "email": email_receive
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@blueprint.route('/check_dup_id', methods=['POST'])
def check_dup_id():
    # 아이디 중복 확인
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})


@blueprint.route('/check_dup_email', methods=['POST'])
def check_dup_email():
    # 이메일 중복 확인
    email_receive = request.form['email_give']
    exists = bool(db.users.find_one({"email": email_receive}))
    return jsonify({'result': 'success', 'exists': exists})



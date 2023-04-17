from flask import Blueprint,request,jsonify
import base64
from DataBase.DB import DB

login_bp = Blueprint('login', __name__, url_prefix='/LogIn')

def base64ToString(b):
    try :
        return base64.b64decode(b).decode("utf-8")
    except :
        return ""
    
##로그인
@login_bp.route('/',methods = ["POST"])
def login():
    #인자 받기
    account = request.values.get('Account')
    aka = request.values.get('AKA')
    town = request.values.get('Town')
    uType = request.values.get('userType')
    card = request.values.get('Card')
    profile = request.values.get('Profile')
    
    conn = DB()
    sql = "INSERT INTO Dreame.UserInfo(UserID,AKA,UserType,Card,Town,UserPhoto)\
        VALUES(%s,%s,%s,%s,%s,%s)"
    res = conn.insert(sql,(account,aka,uType,card,town,profile))
    
    return res
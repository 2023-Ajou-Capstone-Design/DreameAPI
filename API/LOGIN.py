from flask import Blueprint,request,jsonify
import base64
from DataBase.DB import DB
import json

login_bp = Blueprint('login', __name__, url_prefix='/LogIn')
file = open("DataBase/sql.json",encoding = "UTF-8")
sql = json.loads(file.read())
login_sql = sql.get("LogIn")

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
    sql = login_sql.get("/")
    res = conn.insert(sql,(account,aka,uType,card,town,profile))
    
    return res
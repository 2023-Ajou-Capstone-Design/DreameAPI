
from flask import Blueprint,request,jsonify
import base64
from DataBase.DB import DB
import base64

mypage_bp = Blueprint('mypage', __name__, url_prefix='/MyPage')

def base64ToString(b):
    try :
        return base64.b64decode(b).decode("utf-8")
    except :
        return ""
    
    
## 내가 쓴 글 리스트
@mypage_bp.route("/myList",methods = ["POST"])
def FoodshareMyList():
    uID = request.values.get('UserID')
    
    sql = "SELECT * FROM FoodShare WHERE (UserID like %s)"
    conn = DB()
    rows = conn.select(sql,( uID))
    
    keys = ("WritingID","UploadTime","Title","Contents","Photo1","Photo2","Photo3","UserID","Town")
    items = [dict(zip(keys,row)) for row in rows]
    for item in items :
        
        item["WritingID"] = str(item["WritingID"])
        item["UploadTime"] = str(item["UploadTime"])
        item["Title"] = str(item["Title"])
        item["Contents"] = str(item["Contents"])
        item["Photo1"] = base64ToString(item["Photo1"])
        item["Photo2"] = base64ToString(item["Photo2"])
        item["Photo3"] = base64ToString(item["Photo3"])
        item["UserID"] = str(item["UserID"])
        
    data = {
        "total" : len(rows),
        "items" : items
    }
    
    return jsonify(data)

## 닉네임 변경
@mypage_bp.route("/AKA",methods = ["POST"])
def akaChange():
    uId = request.values.get("UserID")
    aka = request.values.get("AKA")
    
    sql = "UPDATE UserInfo SET AKA = %s WHERE UserID like %s"
    conn = DB()
    res = conn.update(sql,(aka,uId))
    return res

## 동네 변경
@mypage_bp.route("/Town",methods = ["POST"])
def townChange():
    uId = request.values.get("UserID")
    town = request.values.get("Town")
    
    sql = "UPDATE UserInfo SET Town = %s WHERE UserID like %s"
    conn = DB()
    res = conn.update(sql,(town,uId))
    return res
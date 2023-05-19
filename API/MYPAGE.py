
from flask import Blueprint,request,jsonify
import base64
from DataBase.DB import DB
from Fucntions.BROWSER import Browser
import base64
import json

mypage_bp = Blueprint('mypage', __name__, url_prefix='/MyPage')
file = open("DataBase/sql.json",encoding = "UTF-8")
sql = json.loads(file.read())
mypage_sql = sql.get("MyPage")

def base64ToString(b):
    try :
        return base64.b64decode(b).decode("utf-8")
    except :
        return ""
    
    
## 내가 쓴 글 리스트
@mypage_bp.route("/myList",methods = ["POST"])
def FoodshareMyList():
    uID = request.values.get('UserID')
    
    sql = mypage_sql.get("myList")
    conn = DB()
    rows = conn.select(sql,( uID))
    
    keys = ("WritingID","UploadTime","Title","Contents","Photo1","UserID","Town")
    items = [dict(zip(keys,row)) for row in rows]
    for item in items :
        
        item["WritingID"] = str(item["WritingID"])
        item["UploadTime"] = str(item["UploadTime"])
        item["Title"] = str(item["Title"])
        item["Contents"] = str(item["Contents"])
        item["Photo1"] = base64ToString(item["Photo1"])
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
    
    sql = mypage_sql.get("AKA")
    conn = DB()
    res = conn.update(sql,(aka,uId))
    return res

## 동네 변경
@mypage_bp.route("/Town",methods = ["POST"])
def townChange():
    uId = request.values.get("UserID")
    town = request.values.get("Town")
    
    sql = mypage_sql.get("Town")
    conn = DB()
    res = conn.update(sql,(town,uId))
    return res

## 카드 잔액조회
@mypage_bp.route("/Card",methods = ["POST"])
def cardCharge():
    uID = request.values.get("UserID")
    sql = mypage_sql.get("getCard")
    conn = DB()
    res = conn.select(sql,(uID))
    
    try :
        if len(res[0][0]) != 16 or res[0][0].isdigit() == False:
            return "Card Error!"
    except :
        return "No Card Number"
    
    br  = Browser()
    br.WaifForLoadPage("https://gdream.gg.go.kr/Login/PointCheck.jsp")
    charge = br.PutData(res[0][0])

    return charge
    
    # return res[0][0]
    
    
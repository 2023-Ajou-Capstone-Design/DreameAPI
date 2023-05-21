from flask import Blueprint,request,jsonify
import base64
from DataBase.DB import DB
import base64
import json

food_bp = Blueprint('foodshare', __name__, url_prefix='/FoodShare')
file = open("DataBase/sql.json",encoding = "UTF-8")
sql = json.loads(file.read())
food_sql = sql.get("FoodShare")

def base64ToString(b):
    try :
        return base64.b64decode(b).decode("utf-8")
    except :
        return ""

## 글 등록
@food_bp.route("/add",methods=["POST"])
def FoodShareAdd():
    #인자 받기
    p1 = request.values.get("Photo1")
    p2 = request.values.get("Photo2")
    p3 = request.values.get("Photo3")
    title = request.values.get("Title")
    contents = request.values.get("Contents")
    userID = request.values.get("UserID")
    town = request.values.get("Town")
    
    sql = food_sql.get("add")
        
    conn = DB()
    res = conn.insert(sql,(title, contents,p1,p2,p3,userID,town))
    
    
    return res

## 글 삭제
@food_bp.route("/del",methods=["POST"])
def FoodShareDel():
    uid = request.values.get("UserID")
    wid = request.values.get("WritingID")
    
    sql = food_sql.get("del")
    conn=DB()
    res = conn.delete(sql,(uid,wid))
        
    return res

## 글 상세
@food_bp.route("/Detail",methods = ["POST"])
def FoodDetail():
    #인자 받기
    wID = request.values.get('WritingID')
    uID = request.values.get('UserID')
    
    sql = food_sql.get("detail")
    conn = DB()
    rows = conn.select(sql,(wID, uID))
    
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
        item["Town"] = str(item["Town"])
    
    data =   {
        "total" : len(rows),
        "items" : items
    } 
    
    return jsonify(data)

## 글 조회
@food_bp.route("/getList",methods = ["POST"])
def FoodShareGetList():
    town = request.values.get("Town")
    
    sql = food_sql.get("getList")
    
    conn = DB()
    rows = conn.select(sql,(town))
    
    keys = ("WritingID","UploadTime","Title","Photo1","UserID","Town")
    items = [dict(zip(keys,row)) for row in rows]
    
    for item in items :
        item["WritingID"] = str(item["WritingID"])
        item["UploadTime"] = str(item["UploadTime"])
        item["Title"] = str(item["Title"])
        item["Photo1"] = base64ToString(item["Photo1"])
        item["UserID"] = str(item["UserID"])
        
    data = {
        "total" : len(rows),
        "items" : items
    }
     
    return jsonify(data)
    
    
## 글 수정
@food_bp.route("/Modify",methods=["POST"])
def FoodShareModify():
    #인자 받기
    p1 = request.values.get("Photo1")
    p2 = request.values.get("Photo2")
    p3 = request.values.get("Photo3")
    title = request.values.get("Title")
    contents = request.values.get("Contents")
    userID = request.values.get("UserID")
    wID = request.values.get("WritingID")
    town = request.values.get("Town")
    
    # sql = "UPDATE FoodShare SET UploadTime = now(), Photo1 =%s, Photo2 = %s, Photo3 = %s, Title = %s, Contents = %s, Town = %s\
    #        WHERE UserID like %s and WritingID = %s"
    sql = food_sql.get("modify")
        
    conn = DB()
    res = conn.update(sql,(p1,p2,p3,title, contents,town, userID, wID))
    
    return res
from flask import Blueprint,request,jsonify
import base64
from DataBase.DB import DB
import base64

food_bp = Blueprint('foodshare', __name__, url_prefix='/FoodShare')

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
    
    sql = "INSERT INTO FoodShare(WritingID, UploadTime, Title, Contents, Photo1, Photo2, Photo3,UserID,Town)\
        VALUES(now(), now(), %s,%s,%s,%s,%s,%s,%s)"
        
    conn = DB()
    res = conn.insert(sql,(title, contents,p1,p2,p3,userID,town))
    
    
    return res

## 글 삭제
@food_bp.route("/del",methods=["POST"])
def FoodShareDel():
    uid = request.values.get("UserID")
    wid = request.values.get("WritingID")
    
    sql = "DELETE FROM FoodShare WHERE (UserID like %s AND WritingID = %s)"
    conn=DB()
    res = conn.delete(sql,(uid,wid))
        
    return res

## 글 상세
@food_bp.route("/Detail",methods = ["POST"])
def FoodDetail():
    #인자 받기
    wID = request.values.get('WritingID')
    uID = request.values.get('UserID')
    
    sql = "SELECT * FROM FoodShare WHERE (WritingID = %s AND UserID like %s)"
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
    
    data =   {
        "total" : len(rows),
        "items" : items
    } 
    
    return jsonify(data)

## 글 조회

## 글 수정
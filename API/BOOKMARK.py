from flask import Blueprint,request,jsonify
import base64
from DataBase.DB import DB
import base64
import json

bookmark_bp = Blueprint('bookmark', __name__, url_prefix='/Bookmark')
file = open("DataBase/sql.json",encoding = "UTF-8")
sql = json.loads(file.read())
bookmark_sql = sql.get("BookMark")

def base64ToString(b):
    try :
        return base64.b64decode(b).decode("utf-8")
    except :
        return ""

## 북마커 추가
@bookmark_bp.route("/add",methods=["POST"])
def BookmarkAdd():
    uid = request.values.get("UserID")
    sid = request.values.get("StoreID")
    stype = request.values.get("StoreType")
    
    conn = DB()
    sql = bookmark_sql.get("add")
    res = conn.insert(sql,(uid,sid,stype))
    
    return res

## 북마커 삭제
@bookmark_bp.route("/del",methods=["POST"])
def BookmarkDel():
    uid = request.values.get("UserID")
    sid = request.values.get("StoreID")
    stype = request.values.get("StoreType")
    
    sql = bookmark_sql.get("del")
    
    conn = DB()
    res = conn.delete(sql,(uid,sid,stype))
    
    return res

## 북마커 리스트
@bookmark_bp.route("/list",methods=["POST"])
def BookmarkList():
    uid = request.values.get("UserID")
    
    sql = bookmark_sql.get("list")
    conn = DB()
    rows = conn.select(sql,(uid))
    
    keys = ("StoreID","StoreType","StorePointLng","StorePointLat","CateName","SubCateName""StoreName","StorePhoto")
    items = [dict(zip(keys,row)) for row in rows]
    for item in items :
        item["StorePhoto"] = base64ToString(item["StorePhoto"])
    
    
    data =   {
        "total" : len(rows),
        "items" : items
    } 
    
    return jsonify(data)
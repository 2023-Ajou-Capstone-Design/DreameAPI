from flask import Blueprint,request,jsonify
import base64
from DataBase.DB import DB
import base64

bookmark_bp = Blueprint('bookmark', __name__, url_prefix='/Bookmark')


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
    sql = "INSERT INTO Bookmarks(UserID,StoreID,StoreType)\
        VALUES(%s,%s,%s)"
    res = conn.insert(sql,(uid,sid,stype))
    
    return res

## 북마커 삭제
@bookmark_bp.route("/del",methods=["POST"])
def BookmarkDel():
    uid = request.values.get("UserID")
    sid = request.values.get("StoreID")
    stype = request.values.get("StoreType")
    
    sql = "DELETE FROM Bookmarks WHERE (UserID like %s AND StoreID like %s AND StoreType like %s)"
    
    conn = DB()
    res = conn.delete(sql,(uid,sid,stype))
    
    return res

## 북마커 리스트
@bookmark_bp.route("/list",methods=["POST"])
def BookmarkList():
    uid = request.values.get("UserID")
    
    sql = "SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreInfo.StorePointLng, StoreInfo.StorePointLat,\
            Tag.CateName, Tag.SubCateName,  StoreDetail.StoreName,StoreDetail.StorePhoto\
            FROM Bookmarks\
            INNER JOIN StoreDetail ON(StoreDetail.StoreID like Bookmarks.StoreID AND StoreDetail.StoreType like Bookmarks.StoreType)\
            INNER JOIN StoreInfo ON(StoreInfo.StoreID like Bookmarks.StoreID AND StoreInfo.StoreType like Bookmarks.StoreType)\
            INNER JOIN Tag ON (StoreInfo.Category like Tag.Category AND StoreInfo.SubCategory like Tag.SubCategory)\
            WHERE Bookmarks.UserID like %s"
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
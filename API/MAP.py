from flask import Blueprint,request,jsonify
import base64
from DataBase.DB import DB
import json

map_bp = Blueprint('map', __name__, url_prefix='/map')
file = open("DataBase/sql.json",encoding = "UTF-8")
sql = json.loads(file.read())
map_sql = sql.get("Map")

def base64ToString(b):
    try :
        return base64.b64decode(b).decode("utf-8")
    except :
        return ""


##사용자 기반 마크 띄우기
@map_bp.route('/MyPosition',methods = ["POST"])
def myposition():
    #인자 받기
    myLng = request.values.get('myPositionLng')
    myLat = request.values.get('myPositionLat')
    mbr = request.values.get('mbr')
    
    sql = map_sql.get("MyPosition")
    conn = DB()
    rows = conn.select(sql,(myLng,myLat,myLng,myLat,mbr))
    
    keys = ("StoreID", "StoreType", "StorePointLng","StorePointLat","StoreName","Distance")
    items = [dict(zip(keys,row)) for row in rows]
    
    data =   {
        "total" : len(rows),
        "items" : items
    } 
    
    return jsonify(data)

## 카테고리 선택했을 때
### 대분류 카테고리 선택했을때
@map_bp.route("/Choose/Category",methods=["POST"])
def ChooseCategory() :
    #인자 받기
    cate = request.values.get('Category')
    myLng = request.values.get('myPositionLng')
    myLat = request.values.get('myPositionLat')
    mbr = request.values.get('mbr')
    
    sql = map_sql.get("ChooseCate")
    conn = DB()
    rows = conn.select(sql,(myLng,myLat,myLng,myLat,mbr,cate))
    
    keys = ("StoreID", "StoreType", "StorePointLng","StorePointLat",
            "CateName","SubCateName","Category","SubCategory","StorePhoto","StoreName","Distance")
    items = [dict(zip(keys,row)) for row in rows]
            
    for item in items :
        item["StorePhoto"] = base64ToString(item["StorePhoto"])
    
    data =   {
        "total" : len(rows),
        "items" : items
    } 
    
    return jsonify(data)

### 소분류 카테고리 선택했을때
@map_bp.route("/Choose/SubCategory",methods=["POST"]) 
def ChooseSubCategory() :
    #인자 받기
    cate = request.values.get('Category')
    subcate = request.values.get('SubCategory')
    myLng = request.values.get('myPositionLng')
    myLat = request.values.get('myPositionLat')
    mbr = request.values.get('mbr')
    
    sql = map_sql.get("ChooseSub")
    conn = DB()
    rows = conn.select(sql,(myLng,myLat,myLng,myLat,mbr,cate,subcate))
    
    keys = ("StoreID", "StoreType", "StorePointLng","StorePointLat",
            "CateName","SubCateName","Category","SubCategory","StorePhoto","StoreName","Distance")
    items = [dict(zip(keys,row)) for row in rows]
            
    for item in items :
        item["StorePhoto"] = base64ToString(item["StorePhoto"])
    
    data =   {
        "total" : len(rows),
        "items" : items
    } 
    
    return jsonify(data)


### 가게 유형 선택했을 때
@map_bp.route("/Choose/StoreType",methods=["POST"]) 
def ChooseStoreType() :
    #인자 받기
    storeType = request.values.get('StoreType')
    myLng = request.values.get('myPositionLng')
    myLat = request.values.get('myPositionLat')
    mbr = request.values.get('mbr')
    
    sql = map_sql.get("ChooseStoreType")
    conn = DB()
    rows = conn.select(sql,(myLng,myLat,myLng,myLat,mbr,storeType))
    
    keys = ("StoreID", "StoreType", "StorePointLng","StorePointLat",
            "CateName","SubCateName","Category","SubCategory","StorePhoto","StoreName","Distance")
    items = [dict(zip(keys,row)) for row in rows]
            
    for item in items :
        item["StorePhoto"] = base64ToString(item["StorePhoto"])
    
    data =   {
        "total" : len(rows),
        "items" : items
    } 
    
    return jsonify(data)

## 키워드 검색시
@map_bp.route("/KeywordSearch",methods = ["POST"])
def KeywordSearch():
    #인자 받기
    keyword = request.values.get('Keyword')
    myLng = request.values.get('myPositionLng')
    myLat = request.values.get('myPositionLat')
    mbr = request.values.get('mbr')
    
    sql = map_sql.get("KeywordSearch")
    conn = DB()
    rows = conn.select(sql,(myLng,myLat,myLng,myLat,mbr,keyword,keyword,keyword))
    
    keys = ("StoreID","StoreType","StorePhoto","StoreName","CateName","SubCateName","StorePointLng","StorePointLat","Category","SubCategory","Distance")
    items = [dict(zip(keys,row)) for row in rows]
    for item in items :
        item["StorePhoto"] = base64ToString(item["StorePhoto"])
    
    data =   {
        "total" : len(rows),
        "items" : items
    } 
    
    return jsonify(data)

## 마커클릭시 가게 클릭시 
@map_bp.route("/StoreDetail",methods = ["POST"])
def StoreDetail():
    #인자 받기
    id = request.values.get('StoreID')
    storeType = request.values.get('StoreType')
    
    sql = map_sql.get("StoreDetail")
    conn = DB()
    rows = conn.select(sql,(id,storeType))
    
    keys = ("StoreID","StoreType","StorePhoto","StoreName",
            "CateName","SubCateName","Address","DetailAddress",
            "DayStart","DayFinish","SatStart","SatFinish","HoliStart","HoliFinish",
            "Item","Provided1","Provided2","Phone","WorkDay")
    items = [dict(zip(keys,row)) for row in rows]
    for item in items :
        item["StorePhoto"] = base64ToString(item["StorePhoto"])
        item["DayStart"] = str(item["DayStart"])
        item["DayFinish"] = str(item["DayFinish"])
        item["SatStart"] = str(item["SatStart"])
        item["SatFinish"] = str(item["SatFinish"])
        item["HoliStart"] = str(item["HoliStart"])
        item["HoliFinish"] = str(item["HoliFinish"])
    
    data =   {
        "total" : len(rows),
        "items" : items
    } 
    
    return jsonify(data)
from flask import Blueprint,request,jsonify
import base64
from DataBase.DB import DB

map_bp = Blueprint('map', __name__, url_prefix='/map')


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
    
    sql = f"SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreInfo.StorePointLng, StoreInfo.StorePointLat,StoreDetail.StoreName,\
            ST_Distance_Sphere(POINT({myLng},{myLat}),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) AS Distance\
            FROM StoreInfo\
            INNER JOIN StoreDetail ON (StoreInfo.StoreID = StoreDetail.StoreID AND StoreInfo.StoreType like StoreDetail.StoreType)\
            WHERE ST_Distance_Sphere(POINT({myLng}, {myLat}),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) <= {mbr}\
            ORDER BY Distance LIMIT 50"
    
    conn = DB()
    rows = conn.select(sql)
    
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
    
    sql = f"SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreInfo.StorePointLng, StoreInfo.StorePointLat,\
            Tag.CateName, Tag.SubCateName, StoreInfo.Category, StoreInfo.SubCategory, StoreDetail.StorePhoto\
            , StoreDetail.StoreName,\
            ST_Distance_Sphere(POINT({myLng}, {myLat}),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) AS Distance\
            FROM StoreInfo\
            INNER JOIN Tag ON (StoreInfo.Category like Tag.Category AND StoreInfo.SubCategory like Tag.SubCategory)\
            INNER JOIN StoreDetail ON (StoreInfo.StoreID = StoreDetail.StoreID AND StoreInfo.StoreType = StoreDetail.StoreType)\
            WHERE ST_Distance_Sphere(POINT({myLng}, {myLat}),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) <= {mbr}\
            AND StoreInfo.Category like {cate}\
            ORDER BY Distance LIMIT 50"
    
    conn = DB()
    rows = conn.select(sql)
    
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
    
    
    sql = f"SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreInfo.StorePointLng, StoreInfo.StorePointLat,\
            Tag.CateName, Tag.SubCateName, StoreInfo.Category, StoreInfo.SubCategory, StoreDetail.StorePhoto\
            , StoreDetail.StoreName,\
            ST_Distance_Sphere(POINT({myLng}, {myLat}),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) AS Distance\
            FROM StoreInfo\
            INNER JOIN Tag ON (StoreInfo.Category like Tag.Category AND StoreInfo.SubCategory like Tag.SubCategory)\
            INNER JOIN StoreDetail ON (StoreInfo.StoreID = StoreDetail.StoreID AND StoreInfo.StoreType = StoreDetail.StoreType)\
            WHERE ST_Distance_Sphere(POINT({myLng}, {myLat}),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) <= {mbr}\
            AND StoreInfo.Category like {cate} AND StoreInfo.SubCategory like {subcate}\
            ORDER BY Distance LIMIT 50"
    
    conn = DB()
    rows = conn.select(sql)
    
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
    
    sql = f"SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreInfo.StorePointLng, StoreInfo.StorePointLat,\
            Tag.CateName, Tag.SubCateName, StoreInfo.Category, StoreInfo.SubCategory, StoreDetail.StorePhoto\
            , StoreDetail.StoreName,\
            ST_Distance_Sphere(POINT({myLng}, {myLat}),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) AS Distance\
            FROM StoreInfo\
            INNER JOIN Tag ON (StoreInfo.Category like Tag.Category AND StoreInfo.SubCategory like Tag.SubCategory)\
            INNER JOIN StoreDetail ON (StoreInfo.StoreID = StoreDetail.StoreID AND StoreInfo.StoreType = StoreDetail.StoreType)\
            WHERE ST_Distance_Sphere(POINT({myLng}, {myLat}),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) <= {mbr}\
            AND StoreInfo.StoreType like {storeType}\
            ORDER BY Distance LIMIT 50"
    
    conn = DB()
    rows = conn.select(sql)
    
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
    
    sql = "SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreDetail.StorePhoto, StoreDetail.StoreName,\
           Tag.CateName, Tag.SubCateName, StoreInfo.StorePointLng, StoreInfo.StorePointLat, StoreInfo.Category, StoreInfo.SubCategory,\
           ST_Distance_Sphere(POINT(%s, %s),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) AS Distance\
           FROM StoreInfo\
           INNER JOIN Tag ON (StoreInfo.Category like Tag.Category AND StoreInfo.SubCategory like Tag.SubCategory)\
           INNER JOIN StoreDetail ON (StoreInfo.StoreID = StoreDetail.StoreID AND StoreInfo.StoreType = StoreDetail.StoreType)\
           WHERE (ST_Distance_Sphere(POINT(%s, %s),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) <= %s AND\
           (StoreDetail.StoreName like  CONCAT('%%', %s, '%%') OR Tag.CateName like  CONCAT('%%', %s, '%%') OR Tag.SubCateName like  CONCAT('%%', %s, '%%')))\
            ORDER BY Distance LIMIT 50"
    
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
    
    sql = "SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreDetail.StorePhoto, StoreDetail.StoreName,\
           Tag.CateName, Tag.SubCateName, StoreDetail.Address, StoreDetail.DetailAddress,\
           StoreDetail.DayStart,StoreDetail.DayFinish, StoreDetail.SatStart, StoreDetail.SatFinish,\
           StoreDetail.HoliStart, StoreDetail.HoliFinish, StoreDetail.Item, StoreDetail.Provided1, StoreDetail.Provided2,\
           StoreDetail.Phone, StoreDetail.WorkDay\
           FROM StoreInfo\
           INNER JOIN Tag ON (StoreInfo.Category like Tag.Category AND StoreInfo.SubCategory like Tag.SubCategory)\
           INNER JOIN StoreDetail ON (StoreInfo.StoreID = StoreDetail.StoreID AND StoreInfo.StoreType = StoreDetail.StoreType)\
           WHERE (StoreInfo.StoreID = %s AND StoreInfo.StoreType like %s)"
    
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
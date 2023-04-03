from flask import Flask, request
import pymysql
import base64

app = Flask(__name__)

def stringToBase64(s) :
    return base64.b64encode(s.encode("utf-8"))

def base64ToString(b):
    return base64.b64decode(b).decode("utf-8")



#접근 테스트
@app.route('/Hello')
def DreameMain() :
    return "Dreame Main"

#지도 관련 기능
##사용자 기반 마크 띄우기
@app.route("/MyPosition",methods=["POST"])
def MyPosition():
    #인자 받기
    myLng = request.values.get('myPositionLng')
    myLat = request.values.get('myPositionLat')
    mbr = request.values.get('mbr')
    
    
    
    #SQL문 작성
    con = pymysql.connect(host='dreame.ceneilkum8gx.us-east-2.rds.amazonaws.com', 
                            user='dreameAdmin', password='dreame9785',
                            db='Dreame', charset='utf8')
    cur = con.cursor()
    sql = "SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreInfo.StorePointLng, StoreInfo.StorePointLat,StoreDetail.StoreName,\
            ST_Distance_Sphere(POINT(%s,%s),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) AS Distance\
            FROM StoreInfo\
            INNER JOIN StoreDetail ON (StoreInfo.StoreID = StoreDetail.StoreID AND StoreInfo.StoreType like StoreDetail.StoreType)\
            WHERE ST_Distance_Sphere(POINT(%s, %s),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) <= %s\
            ORDER BY Distance LIMIT 50"
    cur.execute(sql,(myLng,myLat,myLng,myLat,mbr))
    rows = cur.fetchall()
    keys = ("StoreID", "StoreType", "StorePointLng","StorePointLat","StoreName","Distance")
    items = [dict(zip(keys,row)) for row in rows]
    # print(rows)
    con.close()
    
    return{
        "total" : len(rows),
        "items" : items
    },200

##카테고리 선택했을 때
@app.route("/Category",methods = ["POST"])
def Category():
    #인자 받기
    cate = request.values.get('Category')
    subCate = request.values.get('SubCategory')
    storeType = request.values.get('StoreType')
    myLng = request.values.get('myPositionLng')
    myLat = request.values.get('myPositionLat')
    mbr = request.values.get('mbr')
    
    
    con = pymysql.connect(host='dreame.ceneilkum8gx.us-east-2.rds.amazonaws.com', 
                            user='dreameAdmin', password='dreame9785',
                            db='Dreame', charset='utf8')
    cur = con.cursor()
    sql = "SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreInfo.StorePointLng, StoreInfo.StorePointLat,\
            Tag.CateName, Tag.SubCateName, StoreInfo.Category, StoreInfo.SubCategory, StoreDetail.StorePhoto\
            , StoreDetail.StoreName,\
            ST_Distance_Sphere(POINT(%s, %s),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) AS Distance\
            FROM StoreInfo\
            INNER JOIN Tag ON (StoreInfo.Category like Tag.Category AND StoreInfo.SubCategory like Tag.SubCategory)\
            INNER JOIN StoreDetail ON (StoreInfo.StoreID = StoreDetail.StoreID AND StoreInfo.StoreType = StoreDetail.StoreType)\
            WHERE ST_Distance_Sphere(POINT(%s, %s),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) <= %s\
            AND StoreInfo.Category like %s AND StoreInfo.SubCategory like %s AND StoreInfo.StoreType like %s\
            ORDER BY Distance LIMIT 50"
    cur.execute(sql,(myLng,myLat,myLng,myLat,mbr,cate,subCate,storeType))
    
    rows = cur.fetchall()
    keys = ("StoreID", "StoreType", "StorePointLng","StorePointLat","CateName","SubCateName","Category","SubCategory","StorePhoto","StoreName","Distance")
    items = [dict(zip(keys,row)) for row in rows]
    for item in items :
        item["StorePhoto"] = base64ToString(item["StorePhoto"])
    con.close()
    
    return{
        "total" : len(rows),
        "items" : items
    }

## 키워드 검색시
@app.route("/KeywordSearch",methods = ["POST"])
def KeywordSearch():
    #인자 받기
    keyword = request.values.get('Keyword')
    myLng = request.values.get('myPositionLng')
    myLat = request.values.get('myPositionLat')
    mbr = request.values.get('mbr')
         
    con = pymysql.connect(host='dreame.ceneilkum8gx.us-east-2.rds.amazonaws.com', 
                            user='dreameAdmin', password='dreame9785',
                            db='Dreame', charset='utf8')
    cur = con.cursor()
    sql = "SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreDetail.StorePhoto, StoreDetail.StoreName,\
           Tag.CateName, Tag.SubCateName, StoreInfo.StorePointLng, StoreInfo.StorePointLat, StoreInfo.Category, StoreInfo.SubCategory,\
           ST_Distance_Sphere(POINT(%s, %s),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) AS Distance\
           FROM StoreInfo\
           INNER JOIN Tag ON (StoreInfo.Category like Tag.Category AND StoreInfo.SubCategory like Tag.SubCategory)\
           INNER JOIN StoreDetail ON (StoreInfo.StoreID = StoreDetail.StoreID AND StoreInfo.StoreType = StoreDetail.StoreType)\
           WHERE (ST_Distance_Sphere(POINT(%s, %s),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) <= %s AND\
           (StoreDetail.StoreName like  CONCAT('%%', %s, '%%') OR Tag.CateName like  CONCAT('%%', %s, '%%') OR Tag.SubCateName like  CONCAT('%%', %s, '%%')))\
            ORDER BY Distance LIMIT 50"
    cur.execute(sql,(myLng,myLat,myLng,myLat,mbr,keyword,keyword,keyword))
    
    rows = cur.fetchall()
    keys = ("StoreID","StoreType","StorePhoto","StoreName","CateName","SubCateName","StorePointLng","StorePointLat","Category","SubCategory","Distance")
    items = [dict(zip(keys,row)) for row in rows]
    for item in items :
        item["StorePhoto"] = base64ToString(item["StorePhoto"])
    con.close()
    
    return{
        "total" : len(rows),
        "items" : items
    }


## 마커클릭시 가게 클릭시 
"""
StoreID, StoreType, StorePhoto, StoreName, CateName, SubCateName, 
Address, DetailAddress, DayStart,DayFinish, SatStart, SatFinish, 
HoliStart, HoliFinish, Item, Provided1, Provided2, Phone, WorkDay
"""
@app.route("/StoreDetail",methods = ["POST"])
def StoreDetail():
    #인자 받기
    id = request.values.get('StoreID')
    storeType = request.values.get('StoreType')
         
    con = pymysql.connect(host='dreame.ceneilkum8gx.us-east-2.rds.amazonaws.com', 
                            user='dreameAdmin', password='dreame9785',
                            db='Dreame', charset='utf8')
    cur = con.cursor()
    sql = "SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreDetail.StorePhoto, StoreDetail.StoreName,\
           Tag.CateName, Tag.SubCateName, StoreDetail.Address, StoreDetail.DetailAddress,\
           StoreDetail.DayStart,StoreDetail.DayFinish, StoreDetail.SatStart, StoreDetail.SatFinish,\
           StoreDetail.HoliStart, StoreDetail.HoliFinish, StoreDetail.Item, StoreDetail.Provided1, StoreDetail.Provided2,\
           StoreDetail.Phone, StoreDetail.WorkDay\
           FROM StoreInfo\
           INNER JOIN Tag ON (StoreInfo.Category like Tag.Category AND StoreInfo.SubCategory like Tag.SubCategory)\
           INNER JOIN StoreDetail ON (StoreInfo.StoreID = StoreDetail.StoreID AND StoreInfo.StoreType = StoreDetail.StoreType)\
           WHERE (StoreInfo.StoreID = %s AND StoreInfo.StoreType like %s)"
    cur.execute(sql,(id,storeType))
    
    rows = cur.fetchall()
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
    con.close()
    
    return{
        "total" : len(rows),
        "items" : items
    }
    

if __name__ == "__main__" :
    app.run(debug=True,host='0.0.0.0', port=5000)
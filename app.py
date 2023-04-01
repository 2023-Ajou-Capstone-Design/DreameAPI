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
            ORDER BY Distance LIMIT 100"
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
    # , StoreDetail.StorePhoto <- Base64 문제해결 필요
    sql = "SELECT StoreInfo.StoreID, StoreInfo.StoreType, StoreInfo.StorePointLng, StoreInfo.StorePointLat,\
            Tag.CateName, Tag.SubCateName, StoreInfo.Category, StoreInfo.SubCategory, StoreDetail.StorePhoto\
            , StoreDetail.StoreName,\
            ST_Distance_Sphere(POINT(%s, %s),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) AS Distance\
            FROM StoreInfo\
            INNER JOIN Tag ON (StoreInfo.Category like Tag.Category AND StoreInfo.SubCategory like Tag.SubCategory)\
            INNER JOIN StoreDetail ON (StoreInfo.StoreID = StoreDetail.StoreID AND StoreInfo.StoreType = StoreDetail.StoreType)\
            WHERE ST_Distance_Sphere(POINT(%s, %s),POINT(StoreInfo.StorePointLng, StoreInfo.StorePointLat)) <= %s\
            AND StoreInfo.Category like %s AND StoreInfo.SubCategory like %s AND StoreInfo.StoreType like %s\
            ORDER BY Distance LIMIT 100"
    cur.execute(sql,(myLng,myLat,myLng,myLat,mbr,cate,subCate,storeType))
    rows = cur.fetchall()
    # print(rows)
    keys = ("StoreID", "StoreType", "StorePointLng","StorePointLat","CateName","SubCateName","Category","SubCategory","StorePhoto","StoreName","Distance")
    items = [dict(zip(keys,row)) for row in rows]
    for item in items :
        item["StorePhoto"] = base64ToString(item["StorePhoto"])
    #     print(type(item["StorePhoto"]))
    # print(items)
    con.close()
    
    return{
        "total" : len(rows),
        "items" : items
    }
    

if __name__ == "__main__" :
    app.run(host='0.0.0.0', port=5000)
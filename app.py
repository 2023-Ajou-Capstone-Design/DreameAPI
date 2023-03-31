from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import pymysql

app = Flask(__name__)

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
@app.route('/Category',methods = ["POST"])
def Category():
    pass

if __name__ == "__main__" :
    app.run(host='0.0.0.0', port=5000)
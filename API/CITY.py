from flask import Blueprint,request,jsonify
from DataBase.DB import DB
import base64
import json

city_bp = Blueprint('city', __name__, url_prefix='/City')
file = open("DataBase/sql.json",encoding = "UTF-8")
sql = json.loads(file.read())
city_sql = sql.get("City")

##도 리스트 출력
@city_bp.route("/Do",methods = ["POST"])
def getDoList():
    sql = city_sql.get("Do")
    conn = DB()
    rows = conn.select(sql)
    keys = ("Do")
    items = [dict(zip(keys,row)) for row in rows]
    data = {
        "total" : len(rows),
        "items" : items
    }
    return jsonify(data)

##시 리스트 출력
@city_bp.route("/Si",methods = ["POST"])
def getSiList():
    Do = request.values.get('Do')
    
    sql = city_sql.get("Si")
    conn = DB()
    rows = conn.select(sql,(Do))
    
    keys = ("Si")
    items = [dict(zip(keys,row)) for row in rows]
    data = {
        "total" : len(rows),
        "items" : items
    }
    return jsonify(data)

##시 리스트 출력
@city_bp.route("/GunGu",methods = ["POST"])
def getGunGuList():
    Do = request.values.get('Do')
    Si = request.values.get("Si")
    
    sql = city_sql.get("GunGu")
    conn = DB()
    rows = conn.select(sql,(Do,Si))
    
    keys = ("GunGu")
    items = [dict(zip(keys,row)) for row in rows]
    data = {
        "total" : len(rows),
        "items" : items
    }
    return jsonify(data)
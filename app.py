from flask import Flask

import base64
import datetime as dt
import json

from API import MAP
from API import BOOKMARK



app = Flask(__name__)
app.register_blueprint(MAP.map_bp)
app.register_blueprint(BOOKMARK.bookmark_bp)  
    

# # 푸드쉐어링 관련 기능
# ## 글 등록
# @app.route("/FoodShare/add",methods=["POST"])
# def FoodShareAdd():
#     #인자 받기
#     p1 = request.values.get("Photo1")
#     p2 = request.values.get("Photo2")
#     p3 = request.values.get("Photo3")
#     title = request.values.get("Title")
#     contents = request.values.get("Contents")
#     userID = request.values.get("UserID")
    
#     con = pymysql.connect(host='dreame.ceneilkum8gx.us-east-2.rds.amazonaws.com', 
#                             user='dreameAdmin', password='dreame9785',
#                             db='Dreame', charset='utf8')
#     cur = con.cursor()
#     sql = "INSERT INTO FoodShare(WritingID, UploadTime, Title, Contents, Photo1, Photo2, Photo3,UserID)\
#         VALUES(now(), now(), %s,%s,%s,%s,%s,%s)"
#     cur.execute(sql,(title, contents,p1,p2,p3,userID))
    
#     con.commit()
    
#     con.close()
    
#     return "sucess"

# ## 글 삭제
# @app.route("/FoodShare/del",methods=["POST"])
# def FoodShareDel():
#     uid = request.values.get("UserID")
#     wid = request.values.get("WritingID")
    
#     con = pymysql.connect(host='dreame.ceneilkum8gx.us-east-2.rds.amazonaws.com', 
#                             user='dreameAdmin', password='dreame9785',
#                             db='Dreame', charset='utf8')
#     cur = con.cursor()
#     sql = "DELETE FROM FoodShare WHERE (UserID like %s AND WritingID = %s)"
#     cur.execute(sql,(uid,wid))
    
#     con.commit()
    
#     con.close()
    
#     return "sucess"

# ## 글 상세
# @app.route("/FoodShare/Detail",methods = ["POST"])
# def FoodDetail():
#     #인자 받기
#     wID = request.values.get('WritingID')
#     uID = request.values.get('UserID')
         
#     con = pymysql.connect(host='dreame.ceneilkum8gx.us-east-2.rds.amazonaws.com', 
#                             user='dreameAdmin', password='dreame9785',
#                             db='Dreame', charset='utf8')
#     cur = con.cursor()
#     sql = "SELECT * FROM FoodShare WHERE (WritingID = %s AND UserID like %s)"
#     cur.execute(sql,(wID, uID))
    
#     rows = cur.fetchall()
#     keys = ("WritingID","UploadTime","Title","Contents","Photo1","Photo2","Photo3","UserID")
#     items = [dict(zip(keys,row)) for row in rows]
#     for item in items :
        
#         item["WritingID"] = str(item["WritingID"])
#         item["UploadTime"] = str(item["UploadTime"])
#         item["Title"] = str(item["Title"])
#         item["Contents"] = str(item["Contents"])
#         item["Photo1"] = base64ToString(item["Photo1"])
#         item["Photo2"] = base64ToString(item["Photo2"])
#         item["Photo3"] = base64ToString(item["Photo3"])
#         item["UserID"] = str(item["UserID"])
#     con.close()
    
#     return{
#         "total" : len(rows),
#         "items" : items
#     }

# # ## 글 리스트
# # @app.route("/FoodShare/getList",methods=["POST"])
# # def FoodShareDel():
# #     pass

# # # 로그인

# # 마이페이지
# ## 내가 쓴 글 리스트
# @app.route("/MyPage/myList",methods = ["POST"])
# def FoodshareMyList():
#     uID = request.values.get('UserID')
#     con = pymysql.connect(host='dreame.ceneilkum8gx.us-east-2.rds.amazonaws.com', 
#                             user='dreameAdmin', password='dreame9785',
#                             db='Dreame', charset='utf8')
#     cur = con.cursor()
#     sql = "SELECT * FROM FoodShare WHERE (UserID like %s)"
#     cur.execute(sql,( uID))
    
#     rows = cur.fetchall()
#     keys = ("WritingID","UploadTime","Title","Contents","Photo1","Photo2","Photo3","UserID")
#     items = [dict(zip(keys,row)) for row in rows]
#     for item in items :
        
#         item["WritingID"] = str(item["WritingID"])
#         item["UploadTime"] = str(item["UploadTime"])
#         item["Title"] = str(item["Title"])
#         item["Contents"] = str(item["Contents"])
#         item["Photo1"] = base64ToString(item["Photo1"])
#         item["Photo2"] = base64ToString(item["Photo2"])
#         item["Photo3"] = base64ToString(item["Photo3"])
#         item["UserID"] = str(item["UserID"])
#     con.close()
    
#     return{
#         "total" : len(rows),
#         "items" : items
#     }
#     pass


if __name__ == "__main__" :
    app.run(debug=True,host='0.0.0.0', port=5000)
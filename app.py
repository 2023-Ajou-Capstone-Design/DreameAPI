from flask import Flask

from API import MAP
from API import BOOKMARK
from API import FOODSHARE



app = Flask(__name__)
app.register_blueprint(MAP.map_bp)
app.register_blueprint(BOOKMARK.bookmark_bp)  
app.register_blueprint(FOODSHARE.food_bp) 
    

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
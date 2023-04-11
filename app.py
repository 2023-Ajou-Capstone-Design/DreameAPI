from flask import Flask

from API import MAP
from API import BOOKMARK
from API import FOODSHARE
from API import MYPAGE


app = Flask(__name__)
app.register_blueprint(MAP.map_bp)
app.register_blueprint(BOOKMARK.bookmark_bp)  
app.register_blueprint(FOODSHARE.food_bp) 
app.register_blueprint(MYPAGE.mypage_bp)
    

# # # 로그인


if __name__ == "__main__" :
    app.run(debug=True,host='0.0.0.0', port=5000)
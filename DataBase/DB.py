import pymysql

class DB :
    def __init__(self) :
        self.con = pymysql.connect(host='dreame.ceneilkum8gx.us-east-2.rds.amazonaws.com', 
                            user='dreameAdmin', password='dreame9785',
                            db='Dreame', charset='utf8')
        self.cur = self.con.cursor()
    
    def select(self,sql,args=None) :
        self.cur.execute(sql,args)
        result = self.cur.fetchall()
        self.cur.close()
        self.con.close()
        return result
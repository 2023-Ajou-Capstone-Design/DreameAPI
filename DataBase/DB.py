import pymysql

class DB :
    def __init__(self) :
        self.con = pymysql.connect(host='dreame.ceneilkum8gx.us-east-2.rds.amazonaws.com', 
                            user='dreameAdmin', password='dreame9785',
                            db='Dreame', charset='utf8')
        self.cur = self.con.cursor()
    
    def select(self,sql,args=None) :
        try :
            self.cur.execute(sql,args)
        except :
            return "fail"
        result = self.cur.fetchall()
        self.cur.close()
        self.con.close()
        return result
    
    def insert(self,sql,args=None) :
        try :
            self.cur.execute(sql,args)
        except :
            return "fail"
        self.con.commit()
        self.cur.close()
        self.con.close()
        return "sucess"
    
    def delete(self,sql,args=None) :
        try :
            self.cur.execute(sql,args)
        except :
            return "fail"
        self.con.commit()
        self.cur.close()
        self.con.close()
        return "sucess"
    
    def update(self, sql, args=None) :
        try :
            self.cur.execute(sql,args)
        except : 
            return "fail"
        self.con.commit()
        self.cur.close()
        self.con.close()
        return "sucess"
    
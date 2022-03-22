import pymysql

con = pymysql.connect(host='localhost',user='root', password='vishal', )
crsr = con.cursor()
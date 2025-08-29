import mysql.connector as x

mc=x.connect(host="localhost",user="root",password="qypw2005",database="stu")
cur=mc.cursor()
q="insert into students(sid,sname) values(%s,%s)"
v=(1,"Mainak")
try:
    cur.execute(q,v)
    
    mc.commit()
except:
    mc.rollback()
print(cur.rowcount)    

mc.close
import mysql.connector as x
mc=x.connect(host="localhost",user="root",password="qypw2005",database="emp")
cur=mc.cursor()
sql="insert into students(ID,NAME,CITY,MARKS) values(%s,%s,%s,%s);"
val=(3,"Nikita Gowel","Pune",100)
try:
    cur.execute(sql,val)
    mc.commit()
except:
    mc.rollback()
print(cur.rowcount,"record inserted")
mc.close

import mysql.connector as x
emp2=x.connect(host="localhost",user="root",password="qypw2005",database="emp")
cur=emp2.cursor()
sql='insert into students(id,name,city,marks) values(%s,%s,%s,%s)'
val=(1,"Mainak","kolkata",89)
try:
    cur.execute(sql,val)
    emp2.commit()
except:
    emp2.rollback()
print(cur.rowcount,"record inserted")
emp2.close
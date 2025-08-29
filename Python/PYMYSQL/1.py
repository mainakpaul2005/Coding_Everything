import mysql.connector as x
emp2=x.connect(host="localhost",user="root",password="qypw2005",database="emp2")
cursor=emp2.cursor()
cursor.execute("CREATE TABLE EMPLOYEE(emp_id int, emp_name varchar(25),emp_sal int,emp_dept varchar(2)); ")

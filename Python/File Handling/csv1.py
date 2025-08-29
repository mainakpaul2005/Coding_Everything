import csv

f=open("Stu_info.csv",'w')
s=csv.writer(f)
rs=['RollNo','Name','Section','Marks']
s.writerow(rs)
sr=[]
for i in range(2):
    print("Student Record : ",i+1)
    Rollno=input("Enter Roll no : ")
    Name=input("Enter name : ")
    Section=input("Enter Section : ")
    Marks=input("Enter Marks : ")
    sr=[Rollno,Name,Section,Marks]
    s.writerow(sr)
f.close()

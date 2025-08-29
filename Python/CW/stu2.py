import pickle
stu={}
stufile=open('Stu.dat',"ab+")
ans='y'
while ans=='y':
    rno=int(input("Enter roll no : "))
    name=input("Enter name : ")
    marks=float(input("Enter marks : "))
    stu["Roll no"]=rno
    stu['Name']=name
    stu["Marks"]=marks
    pickle.dump(stu,stufile)
    ans=input("Want to enter more records?")
stufile.close()
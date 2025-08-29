count=int(input("Enter no of students  : "))
file=open("Mark.txt","w+") 
for i in range(count):
    print("Enter details of students  : ")
    roll=int(input("Enter roll no : "))
    name=input("Name :")
    marks=float(input("Marks : "))
    rec=str(roll)+","+name+","+str(marks)+"\n"
    file.write(rec)
file.close()
    
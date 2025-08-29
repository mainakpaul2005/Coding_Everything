stu={}
ans='Y'
while ans=='Y':
     name=input("Enter name:")
     ph=input("Enter phone no :")
     stu[name]=ph
     ans=input("Want to enter more names?(Y/N) ")
print("The created dictonary is : ",stu)
nm=input("Enter name to search for : ")
if nm in stu.keys():
    lst=[nm,stu[nm]]
    print("The requested list is : ",lst)
else:
    print("not found")





        


import csv
f=open("prod.csv",'w',newline='')
n=int(input("Enter No of products to enter:"))
s=csv.writer(f)
s.writerow(['pid','pname','pprice'])
for i in range(n):
    pid=input("Enter Product ID : ")
    pname=input("Enter name of Product : ")
    pprice=int(input("Enter Price of Product : "))
    s.writerow([pid,pname,pprice])
f.close()    
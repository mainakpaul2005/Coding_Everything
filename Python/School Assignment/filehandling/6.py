import csv
f=open("prod.csv","r")
d=csv.reader(f)
next(f)
c=0
sum=0
print(" Product ID","\t","Product name","\t","Product Price")
for i in d:
   c=c+1
   sum=sum+float(i[2])
   print("\t",i[0],"\t",i[1],"\t",i[2])   
avg=sum/c
print("Average Price of Products :",avg)     
f.close()
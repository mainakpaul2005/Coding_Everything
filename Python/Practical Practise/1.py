f=open("Practical Practise/Mainak.txt",'r+')
b=f.readlines()
lst=[]
for i in range(len(b)):
   s=f.readline()
   for i in s:
     if i!=" ":
      lst.append(i)   
print(lst)      
  
      
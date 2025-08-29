f=open("Practical Practise/Mainak.txt",'r+')
lst=[]
s=f.readline()
for i in s:
   if i!=" ":
      lst.append(i)   
for i in lst:
   print(i)
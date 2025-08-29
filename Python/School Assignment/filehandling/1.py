f=open("Delhi.txt",'w+')
rec=[]
ans=1
print("Enter Few Lines about Delhi")
while ans==1:
  t=input()
  rec.append(t)
  ans=int(input("Enter 1 to enter more lines or 0 to exit. "))
for i in rec:
  f.write(i)
  f.write("\n")
f.close()
def remaA():
    with open("Delhi.txt") as F1:
       with open("sub.txt",'w') as F2:
        for i in F1:
         F2.write(i.replace('a' or 'A',''))    
    F2.close
    F1.close  
remaA()    

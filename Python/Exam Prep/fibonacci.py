def fibit(n):
   a,b,c=0,1,0
   l=[0,1]
   for i in range(n-2):
      c=a+b
      l.append(c)
      a,b=b,c
   return l   
t=int(input("Enter No of terms : "))
print(fibit(t))
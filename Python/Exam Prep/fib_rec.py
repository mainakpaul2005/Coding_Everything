def rec_fib(n):
   if n<=1:
      return n 
   else:
      return(rec_fib(n-2)+rec_fib(n-1))
l=[]   
n=int(input("Enter No of terms: "))
if n<0:
   print("Enter Positive Integer : ") 
else:
   for i in range(n):
      l.append(rec_fib(i))
print(l)      

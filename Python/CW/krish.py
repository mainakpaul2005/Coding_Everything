n=int(input("Enter a Number : "))
s=0
t=n
def fact(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res 
while(n>0):
    r=n%10
    f=fact(r)
    s=s+f
    n=n//10
if(s==t):
    print('Krishnamurthy Number ')
else:
    print('Not a krishnamurthy number')        
   
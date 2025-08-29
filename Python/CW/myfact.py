n=int(input("Enter a number :"))
t=n
def fact(n):
    if(n==1 or n==0):
        return n
    else:
        return n*fact(n-1)    
print(t,"! = ",fact(n))       
import math
def my_pow(x,n):
    if len(str(n))==0:
        n=2
        x=int(x)
        return math.pow(x,2)
    else:
        x=int(x)
        n=int(n)
        return math.pow(x,n)
a=input("Enter a number : ")
b=input("Enter its power : ")
print("The value : ",my_pow(a,b))         
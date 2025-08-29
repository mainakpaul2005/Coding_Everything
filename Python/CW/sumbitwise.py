a=int(input("Enter a Number : "))
b=int(input("Enter second number : "))
while(b!=0):
    c=a&b;
    a=a^b
    b=c<<1
print(a)    

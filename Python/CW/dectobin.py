print("Enter a number:",end='')
n=int(input())
def dec2bin(n):
    if n>1:
        dec2bin(n//2)
    print(n%2,end='')
dec2bin(n)    
print()
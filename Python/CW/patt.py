n=5
num=65
k=2*n-2
for i in range(0,n):
    for j in range(0,k):
        print(end=' ')
    k=k-2
    for j in range(0,i+1):    
        print(chr(num),end=' ')
        num=num+1
    print("\r")    

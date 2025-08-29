n=int(input("Enter no. of rows : "))
num=1
for i in range(1,n):
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print("\r")  
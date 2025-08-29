l=eval(input("Enter a List : "))
print("Let the list is ",l)
print("Output:")
def outpat(l):
    n=len(l)
    for i in range(n):
        for j in range(i+1):
           print(l[i],end="")
        print("\r") 
outpat(l)        
#1
#55
#777
#8888    
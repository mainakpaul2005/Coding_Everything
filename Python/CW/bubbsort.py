l=eval(input("Enter a List of numbers : "))

n=len(l)

for i in range(0,n-1):
    for j in range(0,n-1-i):
        if l[j]>l[j+1]:
           l[j],l[j+1]=l[j+1],l[j]

print("Sorted Array: ",l)           
l=eval(input("Enter a List of numbers :"))
max,n,m=0,0,0
min=l[0]
for i in range(0,len(l)-1):
    if l[i]>max:
        max=l[i]
        m=i
    elif min>l[i]:
        min=l[i]
        n=i
print("Max Elemnt in List :",max,"with index :",m)    
print("Min Elemnt in List :",min,"with index :",n)         
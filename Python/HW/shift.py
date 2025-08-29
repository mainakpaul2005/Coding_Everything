arr=eval(input("Enter a List of Numbers : "))
n=len(arr)
a=[]
for i in range(0, n):  
     last = arr[len(arr)-1];  
     for j in range(len(arr)-1, -1, -1):  
          arr[j] = arr[j-1];  
     arr[0] = last
     a=arr  
print(a)
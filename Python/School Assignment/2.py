lst1=eval(input("Enter a list of numbers : "))
lst2=[]
def mymin(l):
    min=l[0]
    for i in l:
        if i<min:
            min=i
    return min        
def checkno(x):
     temp = x
     sum1 = 0
     while (temp != 0):
         r = temp % 10
         sum1 = sum1 + (r**3)
         temp = temp // 10
     if sum1==x:
         return sum1
for i in lst1:
    if checkno(i)==i:
        lst2.append(i) 
print("The no.s which are equal to the sum of the cube of its digits are : ",lst2)
print("The smallest such number is : ",mymin(lst2))       
#Enter a list of numbers : [234,456,654,371,152,153]
#The no.s which are equal to the sum of the cube of its digits are :  [371, 153]
#The smallest such number is :  153    
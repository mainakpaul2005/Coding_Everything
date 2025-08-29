def PUSH(m,lst):
   lst.append(m)
def POP(n,lst):
   for i in range(len(lst)-1):
      if lst[i]==n:
         lst.pop(i)
         print(lst[i])
lst=[21,23,32,43,45]
m=int(input("Enter Marks ; "))
n=23
PUSH(m,lst)
POP(n,lst)
print(lst)
   
   
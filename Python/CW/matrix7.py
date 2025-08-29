r=int(input("Enter no of rows :"))
c=int(input("Enter no of columns : "))
mat=[]
print("Enter elements row wise : ")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    mat.append(a)
for i in range(r):
    for j in range(c):
        print(mat[i][j],end=" ") 
    print()           

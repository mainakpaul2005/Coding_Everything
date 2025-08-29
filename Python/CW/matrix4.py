a=[[1,2],[4,3],[5,6]]
b=[[7,8],[9,10],[0,4]]
res=[[0,0],[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        res[i][j]=a[i][j]+b[i][j]
print(res)        
a=[[1,2],[3,4]]
x=[[5,6],[7,8]]
res=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        res[i][j]=a[i][j]+x[i][j]
for i in range(len(res)):
    print(res)        
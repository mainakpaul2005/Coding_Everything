t=()
a,b,c=0,1,0
t=t+(0,1,)
for i in range(1,8):
    c=a+b
    t=t+(c,)
    a,b=b,c
print("The tuple with the first 9 terms of fibonacci series : ",t)    
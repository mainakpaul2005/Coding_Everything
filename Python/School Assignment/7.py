def Change(N):
    for i in range(len(N)):
        if i%2==0:
            N[i]-=2
        else:
            N[i]+=1
    return N
lst=eval(input("Enter a List : "))
print("After Changing : ",Change(lst))            
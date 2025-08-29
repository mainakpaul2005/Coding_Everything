def my_sum(*ab):
    s=0
    n=len(ab)
    for i in n:
        s=s+ab[i]
return s

ab=[1,2,3,4,5]
print("Sum = ",my_sum(ab))        
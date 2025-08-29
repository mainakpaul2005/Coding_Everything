def myreci(n):
    t=float(n)
    if t==0:
        return "Infinity"
    elif t<0:
        t=-(t)
        rec=-(1/t)
    else:
        rec=(1/t)
    return rec
a=input("Enter a Number : ")
print("The Number is  :",a)
print("The reciprocal of the number is : ",myreci(a))




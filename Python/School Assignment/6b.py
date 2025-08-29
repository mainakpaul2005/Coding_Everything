m=input("Enter a Sentence : ")
def mysplit(s):
    t=s
    sp=input("Enter string to perform split : ")
    t=t.split(sp)
    return t
a=mysplit(m)
print("Before Splitting : ",m)
print("After  Splitting : ",a)

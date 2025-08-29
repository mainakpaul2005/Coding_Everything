try:
    x=int(input("Enter a number: "))
    assert x%2==0
except:
    print("Not even number")
else:
    rec=1/x 
    print("reciprocal :",rec)       
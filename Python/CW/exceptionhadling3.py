try:
    x=int(input("Enter a Number:"))
    y=int(input("Enter a Number: "))
    r=x/y
    print(r)
except:
    print("Zero division error")
finally:
    print("Enter only non zero numbers as denominators.")        
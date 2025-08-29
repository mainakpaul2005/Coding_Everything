import math
print("The General form of a Quadratic equation : ax + bx**2 + c = 0")
a=int(input("Enter 'a' "))
b=int(input("Enter 'b' "))
c=int(input("Enter 'c' "))
print("\n")
print(f"The solution of the Equation : {a}x + {b}x**2 + {c} = 0 are: \n")
d=(b**2)-(4*a*c)
r1=(-b+math.sqrt(d))/(2*a)
r2=(-b-math.sqrt(d))/(2*a)
if d>0:
    print("Type of roots : Distinct and Real roots")
elif d==0:
    print("Type of roots : Real and Equal roots")
else:
    print("Type of roots : Two complex roots")    
print(f"The solutions are {r1} and {r2}")    



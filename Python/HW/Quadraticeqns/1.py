import math
def perfectsqr(a):
    sqr=math.sqrt(a)
    if sqr*sqr == a:
        return a 
print("The General form of a Quadratic equation : ax**2 + bx + c = 0")
a=int(input("Enter coeeficient of x**2 : "))
b=int(input("Enter coefficient of x : "))
c=int(input("Enter constant term :  "))
print("\n")
r1,d,r2,x,y=0,0,0,0,0
if a==0:
    print("The equation is a linear equation.")
    r1=-b/c
else:
    d=(b**2)-(4*a*c)   
    if d>=0:
        if d>0:
            print("Roots are real and equal.")
            r1=(-b+math.sqrt(d))/(2*a)
            r2=(-b-math.sqrt(d))/(2*a)
            print(r1)
            print(r2)
        else:
            print("Roots are real and unequal.")    
            r1=(-b+math.sqrt(d))/(2*a)
            r2=(-b-math.sqrt(d))/(2*a)
            print(r1)
            print(r2)
    else:
        print("Roots are imaginary and unequal.")    
        x=-b/(2*a)    
        y=math.sqrt(d)/(2*a)
        print("Root 1 : ",x,"+","i",y)
        print("Root 1 : ",x,"-","i",y)
    if perfectsqr(d) == d:
        print("Roots are rational ")
    else:
        print("Roots are irrational")      
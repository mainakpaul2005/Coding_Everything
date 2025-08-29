def printPattern(line):
   for i in range(0,line):
     for j in range(0,i+1):
       if j<=i:
        print("#",end=" ")
     print("\r")
n=int(input("Enter no of lines: "))
printPattern(n)  
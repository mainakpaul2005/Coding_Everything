n1=[]
n1=eval(input("Enter a list of numbers : "))
n=[2,4,32,43,45,54]
l=len(n)
def mymax(n):
    max=0
    for i in range(1,l):
        if n[i]>n[i+1]:
            max=n[i]
    print(max) 
mymax(n)
mymax(n1)

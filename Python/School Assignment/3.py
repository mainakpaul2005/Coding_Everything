s=input("Enter a line : ")
def myproj(m):
   m=m.title()
   m=m.split()
   str1=" "
   for i in m:
       str1+=i[:-1]+i[-1].upper()+" "
   return str1    
print("After capitalizing first and last letter of each word :",myproj(s))    
#Enter a line : mainak is my nme
#After capitalizing first and last letter of each word :   MainaK IS MY NmE
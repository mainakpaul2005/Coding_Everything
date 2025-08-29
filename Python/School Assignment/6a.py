m=input("Enter a Sentence : ")
def Tripstr(sen):
    s=sen.split()
    s2=""
    for i in range(len(s)):
       if len(s[i])==3:
          s[i]="***"
          break
    for i in range(len(s)):   
       s2+=s[i]+" "
    return s2   
print("Before : ",m)
print("After  : ",Tripstr(m))

str1=input("Enter a String :")
vowels="aeiouAEIOU"
c=0
for i in str1:
    if i in vowels:
        c+=1
print("No of vowels :",c)            
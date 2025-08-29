f=open("Story.txt","w+")
ans=int(input("Enter no of lines : "))
for i in range(ans):
    l=input("Enter a Sentence : ")
    f.writelines(l)
    f.writelines("\n")
    
    
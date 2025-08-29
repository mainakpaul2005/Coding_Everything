str=input("Enter a Sentence : ")
l=str.split(" ")
for i in l:
    if i=="girl":
        l.remove(i)
        l.append("boy")
for i in l:
    print(i,end=" ")        
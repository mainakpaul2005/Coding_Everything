import pickle

def CreateFile():
    Book=[]
    f=open("Book.dat",'ab+')
    ans='1'
    while int(ans)==1:
        BookNo=int(input("Enter Book Number : "))
        Book_Name=input("Enter Book Name : ")
        Author=input("Enter Name of Author : ")
        Price=int(input("Enter Book Price : "))
        Book=[BookNo,Book_Name,Author,Price]
        pickle.dump(Book,f)
        ans=input("Enter 1 for more records.")
        if f==0:
            break
    f.close()

def CountRec(Author):
    c=0
    f1=open("Book.dat",'rb')
    try:
        while True:
            B=pickle.load(f1)
            if B[2].lower()==Author.lower():
                c+=1
    except EOFError:
        print("No of records of Author : ",c) 
        f1.close()           
CreateFile()
CountRec("RS Aggarwal")

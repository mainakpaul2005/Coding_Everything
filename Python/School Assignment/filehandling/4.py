import pickle
def create_rec():
    f=open("STUDENT.DAT",'ab')
    ans=1
    while ans==1:
        admission_number=int(input("Enter Admission Number : "))
        Name=input("Enter Name of Student : ")
        Percentage=float(input("Enter Percentage : "))
        st=(admission_number,Name,Percentage)
        pickle.dump(st,f)
        ans=int(input("Enter 1 for more records or 0 to exit."))
        if f==0:
            break
        f.close
def count_rec():
    c=0
    f=open("STUDENT.DAT",'rb')
    try:
        while True:
            B=pickle.load(f)
            if B[2]>75:
                c+=1
                print("Admission No:",B[0],"Student Name:",B[1],"Percentage:",B[2])
    except EOFError:
        print("No Of students above 75% :",c) 
        f.close()           


create_rec()
count_rec()
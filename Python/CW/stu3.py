import pickle
stu={}
fin=open("Stu.dat","rb+")
try:
    print("File Stu.dat stores these records : ")
    while True:
        stu=pickle.load(fin)
        print(stu)
except EOFError:
    fin.close()        
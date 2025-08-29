import csv
with open("Stu_info.csv",'r') as f:
    x=csv.reader(f)
    print("Student's Data : ")
    for n in x:
        print(n)
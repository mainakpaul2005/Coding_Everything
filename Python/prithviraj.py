students={
    "Rahul":9876115349,
    "Ankit":7411317643,
    "Surya":7003432967,
    "John":8332413615,
    "Riya":8132896197
}
name=input("Enter a name to search for :")
found_students=[]
if name in students:
    found_students.append((name,students[name]))
else:
    print("Not Found.")
if found_students:
    print("Found the following student:")
    for student in found_students:
        print(f"{student[0]}:{student[1]}")        
ch = input("Do you want to proceed? (y/n) : ")

students = {
    1: {},
    2: {},
    3: {}
}

while(ch == "y" or ch == "Y"):

    print("\n\tMenu:\t")
    print("\t----\t")
    m = int(input("1. Insert and print \n2. Modify Student Age \n3. Add University \n4. Remove Stream \n5. Insert 3 Students \nEnter your choice: "))

    if m == 1:
        name = input("Enter the Student Name: ")
        age = int(input("Enter the Student Age: "))
        stream = input("Enter the Stream: ")
        students[1] = {"name": name, "age": age, "stream": stream}

        for i in students:
            if students[i]:
                print(f"\nDetails of Student {i}:")
                for key, value in students[i].items():
                    print(f"{key.capitalize()}: {value}")

    elif m == 2:
        if 1 in students and "age" in students[1]:
            age = int(input("Enter new age: "))
            students[1]["age"] = age
        else:
            print("No student found to update!")

        for i in students:
            if students[i]:
                print(f"\nDetails of Student {i}:")
                for key, value in students[i].items():
                    print(f"{key.capitalize()}: {value}")

    elif m == 3:
        if 1 in students:
            uni = input("Enter University: ")
            students[1]["University"] = uni
        else:
            print("No student found!")

        for i in students:
            if students[i]:
                print(f"\nDetails of Student {i}:")
                for key, value in students[i].items():
                    print(f"{key.capitalize()}: {value}")

    elif m == 4:
        if 1 in students and "stream" in students[1]:
            del students[1]["stream"]
        else:
            print("No stream found to delete!")

        for i in students:
            if students[i]:
                print(f"\nDetails of Student {i}:")
                for key, value in students[i].items():
                    print(f"{key.capitalize()}: {value}")

    elif m == 5:
        for i in range(1, 4):
            name = input(f"Enter name of Student {i}: ")
            age = int(input(f"Enter age of Student {i}: "))
            stream = input(f"Enter stream of Student {i}: ")
            students[i] = {"name": name, "age": age, "stream": stream}

        for i in students:
            if students[i]:
                print(f"\nDetails of Student {i}:")
                for key, value in students[i].items():
                    print(f"{key.capitalize()}: {value}")

    else:
        print("Invalid Choice!")

    ch = input("\nDo you want to proceed? (y/n) : ")
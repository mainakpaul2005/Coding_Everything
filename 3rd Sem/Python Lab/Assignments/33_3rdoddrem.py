l = eval(input("Enter a list of numbers: "))

c = 0   
new_list = []

for num in l:
    if num % 2 != 0:   
        c += 1
        if c % 3 == 0: 
            continue   
    new_list.append(num)

print("List after removing every 3rd odd number:", new_list)

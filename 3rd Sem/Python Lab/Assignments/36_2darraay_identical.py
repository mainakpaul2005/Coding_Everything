r = int(input("Enter the number of rows for the Array: "))
c = int(input("Enter the number of columns for the Array: "))

m = [[0 for _ in range(c)] for _ in range(r)]

print("Enter the Array:")

for i in range(r):
    for j in range(c):
        m[i][j] = int(input(f"Enter element at row {i+1}, col {j+1}: "))

print("\nThe Array is:")
for row in m:
    print(" ".join(map(str, row)))   # formatted print

# ---- Check identical rows ----
row_f = False
for i in range(r):
    for j in range(i + 1, r):
        if m[i] == m[j]:
            print(f"\nIdentical Rows found: Row {i+1} and Row {j+1}")
            print("Row", i+1, ":", " ".join(map(str, m[i])))
            print("Row", j+1, ":", " ".join(map(str, m[j])))
            row_f = True

# ---- Check identical columns ----
col_f = False
for i in range(c):
    for j in range(i + 1, c):
        identical = True
        for k in range(r):
            if m[k][i] != m[k][j]:
                identical = False
                break
        if identical:
            col_i = [m[k][i] for k in range(r)]
            print(f"\nIdentical Columns found: Column {i+1} and Column {j+1}")
            print("Column", i+1, ":", " ".join(map(str, col_i)))
            print("Column", j+1, ":", " ".join(map(str, col_i)))
            col_f = True

if not row_f and not col_f:
    print("\nNo identical rows or columns found.")

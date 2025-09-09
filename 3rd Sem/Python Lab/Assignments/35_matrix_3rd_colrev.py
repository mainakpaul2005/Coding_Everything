# Input matrix
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

m = []
print("Enter the matrix row by row:")
for i in range(r):
    row = list(map(int, input().split()))
    m.append(row)


# Reverse every 3rd column
for j in range(c):
    if (j + 1) % 3 == 0:  # check 3rd, 6th, 9th ... columns
        # Extract column
        col = [m[i][j] for i in range(r)]
        # Reverse it
        col.reverse()
        # Put back into matrix
        for i in range(r):
            m[i][j] = col[i]

print("\nMatrix with every 3rd column reversed:")
for row in m:
    print(" ".join(map(str, row)))

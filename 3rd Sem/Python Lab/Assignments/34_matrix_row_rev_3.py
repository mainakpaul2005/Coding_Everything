# Input matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter the matrix row by row:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Reverse every 2nd row (i.e., row index 1, 3, 5, ...)
for i in range(rows):
    if (i+1) % 2 == 0:   # check if it's the 2nd, 4th, 6th... row
        matrix[i] = matrix[i][::-1]  # reverse the row

# Output the modified matrix
print("\nMatrix after reversing every 2nd row:")
for row in matrix:
    print(row)

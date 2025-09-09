r, c = map(int, input("Enter rows and cols: ").split())
m = [list(map(int, input().split())) for _ in range(r)]

# Check complementary rows
for i in range(r//2):
    if m[i] == m[-(i+1)][::-1]:
        print(f"Row {i+1} and Row {r-i} are reverse of each other")

# Check complementary columns
for j in range(c//2):
    col1 = [m[i][j] for i in range(r)]
    col2 = [m[i][c-j-1] for i in range(r)]
    if col1 == col2[::-1]:   # reverse check
        print(f"Column {j+1} and Column {c-j} are reverse of each other")

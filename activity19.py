
rows = 5

for i in range(1, rows + 1):
    for s in range(rows - i):
        print("  ", end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for x in range(2, i + 1):
        print(x, end=" ")
    print()

for i in range(rows - 1, 0, -1):
    for s in range(rows - i):
        print("  ", end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for y in range(2, i + 1):
        print(y, end=" ")
    print()
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
target = 5

m = len(matrix)

n = len(matrix[0])

row = 0
col = n - 1

found = False

while row < m and col >= 0:

    if matrix[row][col] == target:
        found = True
        break

    elif matrix[row][col] > target:
        col -= 1

    else:
        row += 1

print(found)

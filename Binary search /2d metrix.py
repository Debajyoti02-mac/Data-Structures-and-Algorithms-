matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 13

m = len(matrix)
n = len(matrix[0])

left = 0
right = m*n-1
found = False

while left <= right:
    mid = (left + right) // 2

    row = mid // n
    col = mid % n

    if matrix[row][col] == target:
        found = True
        break

    elif matrix[row][col] < target:
        left = mid + 1

    else:
        right = mid - 1

print(found)
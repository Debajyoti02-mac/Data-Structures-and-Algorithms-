matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]

k = 8

m = len(matrix)
n = len(matrix[0])

left = matrix[0][0]
right = matrix[m-1][n-1]

while left < right:

    mid = (left + right) // 2

    count = 0

    for i in range(m):
        for j in range(n):

            if matrix[i][j] <= mid:
                count += 1

    if count < k:
        left = mid + 1
    else:
        right = mid

print(left)
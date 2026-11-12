def climbing(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    return climbing(n-1) + climbing(n-2)


print(climbing(5))
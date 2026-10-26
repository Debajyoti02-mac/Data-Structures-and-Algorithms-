nums = [5, 2, 9, 1, 7, 3]
second_min = float('inf')
minimum = float('inf')

for i in nums:
    if i < minimum :
        second_min = minimum 
        minimum = i 
    elif second_min > i and i > minimum :
        second_min = i

print(second_min)
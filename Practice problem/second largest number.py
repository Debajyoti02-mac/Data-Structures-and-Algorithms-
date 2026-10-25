nums = [4, 7, 2, 9, 3, 8]
first = 0 
second = float('inf')
for i in nums:
    if i > first  :
        second = first 
        first = i 
    elif i < first and second < i :
        second = i 
print(second)
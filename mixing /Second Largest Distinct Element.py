nums = [12, 5, 8, 12, 10, 8, 3]
max = 0
second_max = 0 
for i in nums:
    if i > max and i > second_max:
        second_max = max 
        max = i 
    elif i > second_max and i < max:
        second_max = i
        
print(max,second_max)
    
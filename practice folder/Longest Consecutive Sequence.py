nums = [100, 4, 200, 1, 3, 2]

numset = set(nums)
print(numset)

count = 1
max_length = 0 
for num in nums:
    if num-1 not in numset:
        current = num 
        count = 1
        
        while current+1 in numset:
            current+=1
            count+=1
    if max_length < count :
        max_length = count 
print(max_length)

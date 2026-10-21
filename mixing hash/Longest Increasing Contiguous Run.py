nums = [3, 5, 7, 2, 4, 6, 8, 1]

count = 1
max_count = 0 
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count+=1
    else:
        count =1
    if max_count < count :
        max_count = count
print(max_count)
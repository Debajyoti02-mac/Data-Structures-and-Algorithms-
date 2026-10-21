nums = [2, 1, 3, 2, 1, 1, 1]
k = 5
total = 0 
left = 0 
right = 0
max_length = 0 
length = 0
while len(nums)>right:
    total +=nums[right]
    while total > k :
        total -=nums[left]
        left+=1
    if total <= k :
        length = right - left + 1 
        if max_length < length :
            max_length = length 
    right+=1
print(max_length)
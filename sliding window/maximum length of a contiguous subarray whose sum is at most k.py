nums = [2, 1, 3, 2, 4, 1, 1, 5]
k = 3

left = 0 
right = 0 
sum = 0 
length = 0 
max_length = 0
while len(nums) > right :
    sum +=nums[right]
    while sum > k :
        sum-=nums[left]
        left+=1
    if sum <= k :   
        length = right - left + 1
        
    if length > max_length :
        max_length = length 
        
    right+=1
print(max_length)
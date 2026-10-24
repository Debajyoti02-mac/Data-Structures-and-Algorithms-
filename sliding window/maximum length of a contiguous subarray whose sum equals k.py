nums = [2, 1, 1, 2, 3, 1, 1, 1, 4]
k = 5

left = 0 
right = 0 

max_length = 0 
length = 0 
sum = 0 

while right < len(nums):
    sum+=nums[right]
    
    while sum > k :
        sum-=nums[left]
        left+=1
    if sum == k :
        length = right - left +1 
    if length > max_length :
        max_length = length
    right+=1
print(max_length)
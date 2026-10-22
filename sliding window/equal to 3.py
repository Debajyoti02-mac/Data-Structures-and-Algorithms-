nums = [1, 2, 1, 1, 1, 3]
k = 3

left = 0 
right = 0
sum = 0
longest = 0 
length = 0 

while right < len(nums):
    sum +=nums[right]
    
    while sum > k :
        sum-=nums[left]
        left+=1 
    if sum == k :
        length = right - left + 1 
        if length > longest :
            longest = length 
    right +=1 
    
print(longest)
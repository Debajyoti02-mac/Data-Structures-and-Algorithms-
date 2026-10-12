nums = [3, 1, 4, 2, 5, 2, 6]

def function(nums):
    left = 0 
    sum = 0 
    right = 0
    max_count = 0
    target = 8
    
    while right < len(nums):
        sum+= nums[right]
        while sum > target :
            sum -=nums[left]
            left+=1
        if sum <= target:
            length = right - left + 1
        
            if max_count < length :
                max_count = length 
        right+=1 
    return max_count 

print(function([3, 1, 4, 2, 5, 2, 6]))
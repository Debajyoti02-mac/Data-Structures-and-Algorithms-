nums = [2, 1, 3, 2, 4, 1, 5, 2]
def function(nums):
    count = 1 
    max_count = 1 
    left = 0 
    right = 0 
    sum = 0 
    target = 6 
    for i in range(len(nums)):
        sum +=nums[right]
        
        if sum > target:
            sum -= nums[left]
            left+=1 
        elif sum == target :
            count+=1 
            
            length = right - left + 1
            
            if length > max_count:
                max_count = length
            
        right += 1
            
    return max_count
    
print(function(nums=nums))
        

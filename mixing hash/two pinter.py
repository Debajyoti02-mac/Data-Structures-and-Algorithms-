nums = [1, 3, 4, 6, 8, 10]
target = 14

left = 0
right = len(nums) - 1 

while left < right:
    sum = nums[left]+nums[right]
    if sum < target :
        left+=1
    elif sum > target :
        right-=1
    elif sum == target :
        break 
print(left,right)
    
    
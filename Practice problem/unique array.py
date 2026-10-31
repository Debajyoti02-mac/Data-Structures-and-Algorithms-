nums = [1, 1, 2, 2, 3, 3, 4, 5, 5]

left = 0 
right = 1 

while right < len(nums):
    if nums[left] == nums[right]:
        right += 1
    else:
        left += 1
        nums[left] = nums[right]
        right += 1
        
print(nums[:left+1])
print(left+1)
        
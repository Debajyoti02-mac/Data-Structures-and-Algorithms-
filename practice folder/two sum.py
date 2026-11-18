nums = [2, 7, 11, 15]
target = 9

# take two pointer >> 
left = 0
right = len(nums) - 1

# a loop till to right 
while left < right:
    # take a variable to calculate the sum 
    total = nums[left] + nums[right]
    # if the total became the target 
    if total == target:
        print([left , right ])
        break
        # if the total is is lesser than target then up the left 
    elif total < target:
        left += 1

    else:
        # else do the right down 
        right -= 1

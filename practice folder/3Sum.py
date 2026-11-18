nums = [-1, 0, 1, 2, -1, -4]

nums.sort()

for i in range(len(nums)):
    left = i + 1
    right = len(nums) - 1
    
    while left < right :
        total = nums[i] + nums[right] + nums[left]
        if total == 0 :
            print([left , right , i])
            break
        elif total < 0 :
            left +=1
        else:
            right-=1
            

nums = [-1, 0, 1, 2, -1, -4]
# first i need to be sort the data before doing any sum operations 
nums.sort()

# run for loop bec want a extra one item in the for sum problem
for i in range(len(nums)):
    left = i + 1
    right = len(nums)-1
    if i > 0 and nums[i] == nums[i-1]:
        continue
    
    while left < right :
        cal = nums[i] + nums[left] + nums[right] 
        if cal == 0 :
            print([nums[i], nums[left], nums[right]])
            left+=1
            right-=1
        elif cal < 0 :
            left +=1
        else:
            right-=1

            
    
    
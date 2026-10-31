nums = [1, 2, 3, 4, 5, 6, 7, 8]
target = 56

# Those both are for the movement of the pointers 
left = 0 
right = len(nums)-1 

# that veriable for the track the movement of sum of two pointers 
sum = 0 


def fun(nums,target,left,right,sum):
    while left < right :
        # Their both movement 
        sum = nums[left]+nums[right]
        if sum > target :
            # is the sum became the highest then left one item from the top 
            right-=1 
        elif sum < target :
            # is the sum is lower than target then just increase one item in the list 
            left+=1
        else:
            return True 
    return False

print(fun(nums,target,left,right,sum))
        

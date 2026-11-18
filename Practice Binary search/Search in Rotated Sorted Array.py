
nums = [2, 5, 6, 0, 0, 1, 2]
target = 3

left = 0
right = len(nums) - 1

exists = False

while left <= right :
    mid = (left + right)//2 
    
    if nums[mid]==target :
        exists = True 
        break 
    if nums[mid]==nums[left]==nums[right]:
        left+=1
        right-=1
    elif nums[left]<=nums[mid]:
        if nums[left]<=target<nums[mid]:
            right=mid-1
        else:
            left = mid+1
    else:
        if nums[mid]<target<=nums[right]:
            left = mid+1
        else:
            right = mid-1 
print(exists)
            
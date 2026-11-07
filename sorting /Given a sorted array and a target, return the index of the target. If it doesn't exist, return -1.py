nums = [1, 3, 5, 7, 9, 11, 13]
target = 9
get_index = -1

left = 0 
right = len(nums)-1 

mid = 0 

while left<=right :
    mid = (left + right) // 2
    
    if nums[mid] == target:
        get_index = mid
        break
    elif nums[mid] < target :
            left = mid+1
    else:
        right = mid-1 
    
print(get_index)
    
        
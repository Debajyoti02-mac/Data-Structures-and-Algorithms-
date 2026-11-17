nums = [1, 3, 5, 7, 9]
target = 1

get_index = 0 
left = 0 
right = len(nums)-1 

while left <= right :
    mid = (left+right)//2 
    
    if nums[mid] == target :
        get_index = mid 
        break 
    elif nums[mid] > target :
        right = mid - 1 
    else:
        left = mid + 1
print(get_index)
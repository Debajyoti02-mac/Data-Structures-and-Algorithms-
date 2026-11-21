nums = [1, 3, 5, 6]
target = 2

left = 0 
right = len(nums)-1 

get_insert_index = 0
while left<=right :
    mid = (left+right)//2 
    
    if nums[mid] == target :
        get_insert_index = mid
        break 
    elif nums[mid] > target :
        right = mid - 1
    else:
        left = mid + 1 
if get_insert_index == 0 :
    get_insert_index = left 
print(get_insert_index)
        
nums = [1, 3, 5, 6]
target = 7

index_position = -1
left = 0 

right = len(nums)-1 
while left <= right :
    mid = (left+right) // 2 
    
    if nums[mid] == target :
        index_position = mid 
        break 
    elif nums[mid] < target:
        left = mid + 1 
    else:
        right = mid - 1 
if index_position==-1:
    index_position = left
print(index_position)
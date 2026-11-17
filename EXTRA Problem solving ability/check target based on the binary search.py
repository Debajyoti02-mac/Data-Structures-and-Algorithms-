nums = [2, 4, 6, 8, 10, 12, 14]
target = 12

left = 0 
right = len(nums)-1 

find = False 
get__index = 0 
while left <= right :
    mid = (left+right)//2 
    if nums[mid] == target :
        find = True 
        get__index = mid 
        break 
    elif nums[mid] < target :
        left = mid +1 
    else:
        right = mid - 1
print(find , get__index)
        
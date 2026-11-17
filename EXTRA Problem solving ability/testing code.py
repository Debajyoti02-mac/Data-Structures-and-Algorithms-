nums = [2, 4, 6, 8, 10, 12, 14]
target = 15

left = 0 
right = len(nums)-1 

get_index_positon = None

while left <= right :
    mid = (left+right)//2 
    if nums[mid]==target :
        get_index_positon = mid 
        break 
    elif nums[mid] > target :
        right = mid - 1 
    else:
        left = mid +1 
if get_index_positon == None :
    print("Value currently not find out in the given array")
else:
    print(f"the possition find out : {get_index_positon}")
    

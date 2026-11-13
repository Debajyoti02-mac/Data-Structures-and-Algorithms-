nums = [1, 3, 5, 6]
left  = 0
right = len(nums)-1
target = 5
get_index = -1


while left <= right :
    mid  = (left+right)//2

    if nums[mid] == target :
        get_index = mid
        break
    elif nums[mid] < target :
        left = mid+1
    else :
        right = mid-1
if get_index == -1 :
    get_index = left
print(get_index)

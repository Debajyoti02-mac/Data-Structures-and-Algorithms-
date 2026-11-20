nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
# Output: True

left = 0 
right = len(nums)-1
find = False
while left < right :
    mid = (left+right)//2 
    if nums[mid]==target :
        find = True 
        break
    elif nums[mid]>target :
        right = mid - 1 
    else:
        left = mid + 1
print(find)
        
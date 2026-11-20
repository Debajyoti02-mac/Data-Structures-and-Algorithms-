nums = [5, 7, 7, 8, 8, 10]
target = 8

first = -1 
last = -1

left = 0 
right = len(nums)-1

while left <= right :
    mid = (left+right)//2 
    if nums[mid]== target :
        right = mid - 1
        first = mid 
    elif nums[mid]>target :
        right = mid - 1
    else:
        left = mid + 1
        
        
        
left = 0 
right = len(nums)-1

while left <= right :
    mid = (left+right)//2 
    if nums[mid]== target :
        left = mid + 1
        last = mid 
    elif nums[mid]>target :
        right = mid - 1
    else:
        left = mid + 1
print([first,last])
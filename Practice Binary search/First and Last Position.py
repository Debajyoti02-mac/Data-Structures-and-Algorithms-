# check the first and last elements's position in the array 
nums = [1, 2, 2, 2, 3, 4, 5]
target = 2

left = 0 
right = len(nums)-1 

first = -1 
last = -1 

while left <= right :
    mid = (left+right)//2 
    if nums[mid]==target:
        right= mid - 1
        first = mid 
        
    elif nums[mid]>target :
        right = mid - 1 
    else:
        left = mid + 1

left = 0 
right = len(nums)-1 
while left <= right :
    mid = (left+right)//2 
    if nums[mid]==target:
        left= mid + 1
        last = mid 
        
    elif nums[mid]>target :
        right = mid - 1 
    else:
        left = mid + 1
print([first,last])
nums = [5, 7, 7, 8, 8, 10]
target = 8

# first save the first ...
first = -1
left , right = 0 , len(nums)-1 
while left <= right :
    mid = (left+right)//2 
    if nums[mid]==target:
        right = mid - 1 # that bec it store the end if it find the second time value 
        first = mid
    elif nums[mid] > target:
        right = mid - 1 
    else:
        left=mid+1
        
# then the last ...
last = -1
left , right = 0 , len(nums)-1 
while left <= right :
    mid = (left+right)//2 
    if nums[mid]==target:
        left = mid + 1 # this increse the previous 
        last = mid
    elif nums[mid] > target:
        right = mid - 1 
    else:
        left=mid+1
print([first,last])

        
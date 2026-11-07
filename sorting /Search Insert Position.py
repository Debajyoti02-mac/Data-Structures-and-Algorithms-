nums = [1, 3, 5, 6]
target = 2
get_item = -1
left = 0 
right = len(nums)-1 
mid = 0
while left<= right :
    mid = (left+right)//2 
    
    if nums[mid] == target :
        get_item = mid 
        break
    elif nums[mid] < target :
        left =mid + 1 
    else:
        right= mid - 1 
if get_item==-1:
    get_item = left
    
   
print(get_item)
        
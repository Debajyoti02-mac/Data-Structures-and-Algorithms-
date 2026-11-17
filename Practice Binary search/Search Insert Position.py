# Search element if it exist on the list either check where it should be place in the list and return out the index 
nums = [1, 3, 5, 6]
target = 2

# left contain first element and right contains before last elemnt into it 
left = 0 
right = len(nums)-1 
# take a var to store the index ..
pos = None 

# run continue until the left became right okay .. 
while left <=right :
    """ 
    IN binary search basically mid is the main point in this okay : >> 
    Mid basically use to show that the elememnt is lower than mid or higher than mid .. and it checks it and adjustable itself by
    using left and right 
    """
    mid = (left+right)//2 
    if nums[mid] == target :
        # if done then break 
        pos = mid 
        break 
    elif nums[mid]>target :
        # if mid became high then check the right and drop the mid 
        right = mid - 1 
    else:
        # else up the left until it became right equal 
        left = mid + 1 
        
# it the pos is none then take the left because left basically do that >> it represent the current insertion position 
if pos == None :
    pos = left 
print(pos)
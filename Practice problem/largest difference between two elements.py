nums = [3, 8, 2, 10, 5, 7, 1]
# For store the max distance 
max_difference = 0 

# get out the min value from the list 
min_element = float('inf')

# This value repeatly check the distance of min element to all element 
distance_became = 0 


for i in range(len(nums)):
    
    # get min element first 
    if nums[i] < min_element:
        min_element = nums[i]
    # distance caught 
    distance_became = nums[i] - min_element 
    # get out the maximum distance 
    if distance_became > max_difference :
        max_difference = distance_became 
print(max_difference)

        
        
    

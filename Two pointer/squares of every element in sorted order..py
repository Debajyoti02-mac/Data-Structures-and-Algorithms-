nums = [-7, -3, 1, 4, 8]

# its start from index zero 
left = 0 
# its the final value in the list 
right = len(nums)-1 

# Taking a empty list that contains the same max value in the given list 
result = [0]*len(nums)

# position basically moving 
position = len(nums)-1 

# a loop that move forward based on the index on the list 
for i in range(len(nums)):
    
    # if the positive left is lower than right 
    if abs(nums[left]) < abs(nums[right]) :
        # then result 8 index contain the squre of it 
        result[position] = nums[right]**2 
        
        # right -=1 so one element drop
        right-=1
        # position -1 basically one area or index drop in the result list 
        position-=1
        
        # or 
    else:
        # same with the left 
        result[position] = nums[left]**2
        left+=1
        position-=1
print(result)

        
    
    

        
    
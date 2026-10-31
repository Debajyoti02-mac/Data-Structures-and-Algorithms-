nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
total = 0 

# empty list to store the elements in the valid in the existing list 
result = []
for i in range(len(nums)):
    # i+1 bec it also grow with the i move forward 
    left = i+1
    right = len(nums)-1
    while left < right :
    # sum of three items store in the veriable 
        total = nums[i] + nums[left] + nums[right]
    
    # if the total is higher than target drop one from the peak 
        if total > target :
            right-=1
       
    # if the total is less then the target give a force in left 
        elif total < target:
            left+=1
        
        else:
            result.append([nums[i], nums[left], nums[right]])
            right-=1
            left+=1
print(result)  
        
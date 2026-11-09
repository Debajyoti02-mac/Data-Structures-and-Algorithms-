nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

#Kadane's Algorithm : >> 

""" 
Their basically Happening >> 

Run a loop al over the given list . then check the max of nums[i] then the max out -2, current_sum = 0 ,  -2 = -2 

thats like eveything calculate 

"""
max_sum = nums[0]
current_sum = nums[0]


for i in range(len(nums)):
    current_sum = max(nums[i], current_sum + nums[i])
    if max_sum < current_sum :
        max_sum = current_sum
print(max_sum)
        
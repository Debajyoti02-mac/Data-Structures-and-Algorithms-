nums = [9, 4, 7, 2]

min_index = 0
""" 
so in selection sort basically happening that >> 

we at last find the index of the minimum value element . then swap it into the fast and thats like goes on ... 

"""
for i in range(len(nums)):
    if nums[i] < nums[min_index]:
        min_index = i
nums[0] , nums[min_index] = nums[min_index] , nums[0]
print(nums)
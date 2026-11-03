nums = [5, 2, 8, 1, 3]
lenght = len(nums)-1
"""
Listen how it working : 

basically it run over the len of nums the original array okay ... 
then we use the innerside loop / nasted loop it basically prevent the out of the range concepts .. 
then we basically take one by one element based on previous element is bigger or not if bigger then swape it ....

"""
for j in range(len(nums)):
    for i in range(lenght):
        if nums[i] > nums[i+1]:
            nums[i] , nums[i+1] = nums[i+1] , nums[i]
print(nums)
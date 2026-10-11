nums = [2, -5, 4, 3, -1, 2] 
## Count when the sum get positive 
def positive_seq(nums):
    count=0
    for i in range(1,len(nums)):
        sum = nums[i]+nums[i-1]
        if sum > 0:
            count+=1 
    return count 

print(positive_seq(nums=nums))

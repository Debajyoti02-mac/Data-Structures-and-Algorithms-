nums = [2, 3, 5, 7, 4, 9, 11, 13, 15, 6] 

## Get the max number line of odds 
def longest_odd(nums):
    count = 0 
    max_count = 0 
    for i in range(1,len(nums)):
        if nums[i]%2!=0:
            count+=1
        else:
            count=0
        if max_count<count:
            max_count=count 
    return max_count 
print(longest_odd([2, 3, 5, 7, 4, 9, 11, 13, 15, 6]))
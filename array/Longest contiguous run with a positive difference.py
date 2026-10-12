nums = [3, 5, 8, 2, 4, 7, 9, 1] 

def longest_positive(nums):
    count = 1
    max_count = 0  
    sum = 0 
    for i in range(0,len(nums)):
        sum = nums[i]-nums[i-1]
        if sum > 0 :
            count+=1 
        else:
            count = 1
        if max_count < count:
            max_count = count 
    return max_count 
print(longest_positive([3, 5, 8, 2, 4, 7, 9, 1] ))
    
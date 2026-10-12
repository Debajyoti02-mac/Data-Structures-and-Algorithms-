nums = [2, 7, 8, 3, 9, 6, 4, 10, 11]

def longest_more_than_5(nums):
    count = 0 
    max_count = 0 
    for i in range(len(nums)):
        if nums[i]>5:
            count+=1
        else:
            count = 0 
        if count > max_count:
            max_count = count
    return max_count 

print(longest_more_than_5(nums=nums))
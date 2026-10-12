nums = [4, 6, 9, 3, 5, 7, 2, 8, 10, 12, 1]
def longest(nums):
    count = 1
    max_count = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1] :
            count += 1
        else:
            count=1 
        if max_count < count:
            max_count = count 
    return max_count 

print(longest([4, 6, 9, 3, 5, 7, 2, 8, 10, 12, 1]))
            
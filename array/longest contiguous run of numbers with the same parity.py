nums = [2, 4, 7, 9, 6, 8, 10, 3, 5] 

def longest(nums):
    count = 1
    max_count = 1
    for i in range(1, len(nums)):
        if nums[i] % 2 == nums[i-1] % 2:
            count += 1
        else:
            count = 1

        if count > max_count:
            max_count = count
    return max_count

print(longest(nums=nums))
        
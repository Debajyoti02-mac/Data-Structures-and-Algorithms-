freq = {}

nums = [1, 2, 3, 1]

def contains_duplicate(nums):
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for i in freq:
        if freq[i] > 1:
            return True
    return False

print(contains_duplicate(nums))
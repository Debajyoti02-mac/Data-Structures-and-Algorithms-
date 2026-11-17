def contains_duplicates(nums):
    frequency = {}
    count = 0

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

        if frequency[num] <= 2:
            count +=1
            return True , count
        else:
            return False , count
    return frequency
print(contains_duplicates([1,2,2,4]))

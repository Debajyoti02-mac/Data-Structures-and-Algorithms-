nums = [12, 5, 8, 12, 3, 10, 8, 6]
'''Basically i did at first store the max in to highest and before that the previous highest store into second largest'''


def second_largest(nums):
    seen = []
    
    for i in nums:
        if i not in seen :
            seen.append(i)
    
    second_largest = float('-inf')
    highest = float('-inf') 
    for i in seen:
        if i > highest:
            second_largest = highest 
            highest = i  
        elif i > second_largest:
            second_largest = i
    return second_largest

print(second_largest(nums=nums))
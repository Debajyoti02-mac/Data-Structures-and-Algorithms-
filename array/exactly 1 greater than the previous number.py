nums = [1, 2, 3, 7, 8, 2, 3, 4, 5, 1]
def Consecutive(nums):
    count = 1 
    max_count = 1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]+1:
            count+=1
        else:
            count=1
        if count > max_count :
            max_count = count 
    return max_count , count 

print(Consecutive([1, 2, 3, 7, 8, 2, 3, 4, 5, 1]))
            
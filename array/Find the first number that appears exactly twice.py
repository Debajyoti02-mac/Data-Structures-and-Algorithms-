nums = [4, 2, 7, 2, 9, 4, 5, 7, 3]


def twice(nums):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen :
            seen[nums[i]]+=1
        else:
            seen[nums[i]]=1 
        
        if seen[nums[i]] == 2 :
            return nums[i]
print(twice([4, 2, 7, 2, 9, 4, 5, 7, 3]))
        


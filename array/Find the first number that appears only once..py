nums = [5, 3, 5, 2, 3, 8, 2, 9, 8, 7]

def find_first(nums):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen :
            seen[nums[i]]+=1
        else:
            seen[nums[i]]=1 
            
    for num in nums:
        if seen[num]==1:
            return num
    
print(find_first([5, 3, 5, 2, 3, 8, 2, 9, 8, 7]))
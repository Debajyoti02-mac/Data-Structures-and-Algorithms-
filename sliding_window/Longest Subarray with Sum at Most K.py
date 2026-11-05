nums = [2, 1, 5, 1, 3, 2]
k = 7

left = 0 
right = 0 

count = 0 
sum = 0 

length = 0 
""" 
Their basically happening >> 
sum contains one by one item then in second nasted while loop --> 
when the sum became greater than the 7 .. 
then remove one item from the end . so left 0 - 1 and also increment left+=1 so it cant be negetive ... 
if sum became the same of the K then count the max ... (right-left+1) how much right it moves and how much left it moves and then + 1 for the calculation ...

"""
while right < len(nums):
    sum+=nums[right]
    
    while sum>k:
        sum-=nums[left]
        left+=1 
        
    length = (right-left+1)
    if length > count : 
        count = length 
        
    right+=1 
    
print(count)
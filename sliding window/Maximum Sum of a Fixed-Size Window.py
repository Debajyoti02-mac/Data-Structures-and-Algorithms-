nums = [2, 1, 5, 1, 3, 2]
k = 3

"""
Here is len(nums)-k+1 reason is 
len of nums is always 6 - k became 3 and +1 just implement one more 
i want to get the calculations of three nums so we have to do this 
"""
def sliding_problem(nums,k):
    max_sum = 0 
    for i in range(len(nums)-k+1):
        sum = 0 
        window = nums[i:i+k]
        for i in window:
            sum +=i
        if max_sum < sum :
            max_sum = sum 
    return max_sum  

print(sliding_problem(nums,k))

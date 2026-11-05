nums = [2, 1, 3, 4, 2, 3, 1, 1]
k = 4

min_sum = float('inf')

for i in range(len(nums) - k +1):
    sum = 0 
    window = nums[i:i+k]
    for i in window:
        sum+=i
    if sum < min_sum:
        min_sum = sum 
print(min_sum)
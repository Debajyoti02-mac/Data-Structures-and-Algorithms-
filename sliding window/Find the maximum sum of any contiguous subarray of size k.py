nums = [3, 8, 2, 5, 7, 6]
k = 3

max_sum = 0

for i in range(len(nums)-k+1):
    sum = 0 
    subarray = nums[i:i+k]
    for i in subarray:
        sum+=i
    if sum > max_sum :
        max_sum = sum 
print(max_sum)
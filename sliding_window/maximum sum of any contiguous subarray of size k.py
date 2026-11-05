nums = [2, 1, 5, 1, 3, 2]
k = 3

minimum  = float('inf')
for i in range(len(nums)-k+1):
    sum = 0
    window = nums[i:i+k] 
    for i in window:
        sum+=i 
    if minimum > sum :
        minimum = sum        
print(minimum)

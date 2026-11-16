nums = [1, 1, 1]
k = 2
cal = 0
for i in range(len(nums)-k+1):
    window = nums[i:i+k]
    for j in window:
        cal+=j
    if cal == k :
        print(True)


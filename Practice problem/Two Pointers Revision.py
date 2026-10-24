nums = [4, 1, 7, 3, 9, 2]
seen = []
left = len(nums) - 1 
for i in range(len(nums)) :
    seen.append(nums[left])
    left-=1
print(seen)
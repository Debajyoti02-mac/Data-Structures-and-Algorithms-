nums = [0, 3, 0, 2, 5, 0, 1] 
seen = []
state = 0 
for i in range(len(nums)):
    if nums[i]!=0:
        seen.append(nums[i])
        state+=1
for i in range(state,len(nums)):
    seen.append(0)
print(seen)

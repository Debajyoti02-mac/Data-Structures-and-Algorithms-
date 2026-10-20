nums = [0, 4, 0, 2, 7, 0, 3]
seen = []
increase = 0
for i in range(len(nums)):
    if nums[i]!= 0:
        seen.append(nums[i])
        increase+=1
for i in range(increase,len(nums)):
    seen.append(0)
print(seen)
    
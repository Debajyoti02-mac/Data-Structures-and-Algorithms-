nums = [2, -5, 4, 3, -1, 2] 
pair_sum = 0 
count = 0
## Count when the sum get positive 
for i in range(1,len(nums)):
    pair_sum=nums[i]+nums[i-1]
    if pair_sum >=0 :
        count+=1
print(pair_sum,count)

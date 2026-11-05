nums = [5, 2, 8, 1, 3]
# copare and swape .. items one by one . thats called bubble sorting ..
for j in range(len(nums)):
    for i in range(len(nums)-1):
        if nums[i] > nums [i+1] :
            nums[i] , nums [i+1] = nums[i+1] , nums[i]
print(nums)
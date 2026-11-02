nums = [0, 1, 0, 3, 12]

count = 0 

for i in range(len(nums)):
    if nums[i]!=0:
        """ 
        so basically in here we can see that if the nums[i] the element isnt 0 then 
        we are basically doing move withing value adding 
        how its happening : >>
        Basically nums[count] its zero = nums[i] its 1 
        then nums[count] is 1 = nums[i] then its became 3 
        then nums[count] is 2 = nums[i] then its became 12 
        
        """
        
        nums[count] = nums[i]
        count+=1 
for i in range(count,len(nums)):
    nums[i]=0 
print(nums)
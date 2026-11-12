nums = [1, 2, 3, 4]

left = 0 
right = len(nums)-1

prefix = []
suffix = []
product_p =1 
product_s = 1
result = []

for i in range(len(nums)):
    prefix.append(product_p)
    product_p*=nums[left] 
    
    left+=1 
print(prefix)

for i in range(len(nums)):
    suffix.append(product_s)
    product_s*=nums[right]
    
    right-=1
print(suffix)

suffix.reverse()
for i in range(len(nums)):
    result.append(prefix[i]*suffix[i])
print(result)



    
nums = [1, 2, 3, 4]
prefix = []
product = 1
multi = 0 
left = 0
# Prefix  >> left to right multiplications 
for i in range(len(nums)):
    prefix.append(product)
    product *= nums[left]
    left+=1

print(prefix)

# Suffix >> right to left multiplication 
prod = 1
right = len(nums)-1 
suffix = []
for i in range(len(nums)):
    suffix.append(prod)
    prod*=nums[right]
    right-=1 
print(suffix)
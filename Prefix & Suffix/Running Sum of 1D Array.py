nums = [1, 2, 3, 4]
array = []
left = 0 
product = 0

for i in range(len(nums)):
    product+=nums[left]
    array.append(product)
    left+=1 
print(array)
nums = [2, 3, -2, 4 ]
left = 0
product = 1 
count = 0
max_element = 0
mini_product = float('inf')
max_count = 0 
for i in range(len(nums)) :
    product *=nums[left]
    if product > 0 : 
        count+=1 
    else:
        count = 1 
    left+=1
    if max_element < product:
        max_element = product
        max_count = count
    elif mini_product > product:
        mini_product = product
    
    print(max_element ,max_count , mini_product)
    
        
        
        
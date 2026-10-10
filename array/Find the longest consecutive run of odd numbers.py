nums = [2, 3, 5, 7, 4, 9, 11, 13, 15, 6] 
count = 0 
max_count = 0 

## Get the max number line of odds 
for i in range(len(nums)):
    if nums[i]%2!=0:
        count+=1 
    else :
        count=0
    if max_count < count :
        max_count = count
print(max_count)
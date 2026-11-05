nums = [1, 0, 1, 1, 0, 1, 1, 1]
left = 0 
right = 0 
count = 0
seen = []
length = 0
while right < len(nums):
    seen.append(nums[right])
    if seen[right] == 0 :
        count+=1
        while  count > 1:
            if seen[left]==0:
                count-=1
            left+=1 
    
    length = max(length , right - left + 1 )
            
    right+=1
print(count  , length)
        
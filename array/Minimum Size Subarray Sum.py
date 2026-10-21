nums = [2, 3, 1, 2, 4, 3]
target = 7

left = 0 
right = 0 

min_length = float('inf')
get = 0 
length  = 0 

'''

Explation : 
both start with zero right get increment easily bec one by one it calculate so right+=1 
and then see that if the get became bigger than total / sum then we substract the left from it using get-=nums[left]
but left+=1 to remove one by one element until it became the same with target/total .
then if it became true then we get the result 

length = right - left + 1 
if right became 5 - 2 + 1 
so the length became like 4 
thats like 

'''

while right < len(nums):
    get +=nums[right]
    
    while  get >= target :
        length = right - left + 1 
        if min_length > length:
            min_length = length
        get-=nums[left]
        left+=1 
        
    right+=1
print(min_length)

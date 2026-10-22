nums = [1, 2, 1, 3, 4, 3, 3]

# freq = {}
left = 0
max_length = 0 
# for i in range (len(nums)):
#     if nums[i] in freq:
#         freq[nums[i]]+=1 
#     else:
#         freq[nums[i]]=1 
#     if len(freq)>2:
#         value = nums[left] 
#         freq[value]-=1 
#         left+=1 
#         if freq[value] == 0 :
#             del freq[value]
#         max_length = max(max_length,i-left+1)
# print(max_length)
            
seen = []

for i in range(len(nums)):
    seen.append(nums[i])
    while len(set(seen))>2:
        seen.pop(0)
        left+=1
    if len(set(seen))==2:
        
        if len(seen)>max_length:
            max_length = len(seen)
print(seen)
print(max_length)

    
        
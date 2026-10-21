nums = [1, 2, 1, 2, 3]
freq = {}
left = 0
max_length = 0 
for i in range(len(nums)):
    if nums[i] in freq:
        freq[nums[i]]+=1
    else:
        freq[nums[i]]=1 
    while len(freq)>2:
        value = nums[left]
        freq[value]-=1
        if freq[value] == 0:
            del freq[value]
        left+=1
    max_length = max(max_length , i - left + 1 )
print(max_length)

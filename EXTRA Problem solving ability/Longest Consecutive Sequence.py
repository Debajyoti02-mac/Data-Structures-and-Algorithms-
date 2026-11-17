nums = [10, 11, 12, 20, 21, 22, 23, 24]
num_set = set(nums)

max_len = 0
count = 1

for num in nums:
    if num-1 not in num_set:
        count+=1
        current = num
        count = 1

        while current+1 in num_set:
            current+=1
            count+=1
    if max_len < count:
        max_len = count
print(max_len)
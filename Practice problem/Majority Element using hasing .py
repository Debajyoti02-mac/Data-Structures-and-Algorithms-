nums = [3, 2, 3]

freq = {}

for  num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for i in nums:
    if freq[i] > len(nums) // 2:
        print(i)
        break
nums = [2, 7, 11, 15]
target = 9

freq = {}

for i in range(len(nums)):
    get = target - nums[i]

    if get in freq:
        print([freq[get], i])
        break

    freq[nums[i]] = i
print(freq)
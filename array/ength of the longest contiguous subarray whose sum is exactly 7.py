nums = [4, 2, 0, 3, 2, 5, 0, 1]
count = 0
target = 7
sum = 0

left = 0
right = 0
max_length = 0

while right < len(nums):
    sum += nums[right]

    while sum > target:
        sum -= nums[left]
        left += 1

    if sum == target:
        count += 1
        length = right - left + 1

        if length > max_length:
            max_length = length

    right += 1

print(max_length)
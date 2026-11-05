nums = [2, 3, 1, 2, 4, 3]
target = 7

min_length = float('inf')
left = 0
right = 0
sum = 0

while right < len(nums):
    sum += nums[right]

    while sum >= target:
        min_length = min(min_length, right - left + 1)
        sum -= nums[left]
        left += 1

    right += 1

print(min_length if min_length != float('inf') else 0)
nums = [1, 1, 2, 2, 3, 4, 4, 5]

left = 0

for right in range(1, len(nums)):
    if nums[left] != nums[right]:
        left += 1
        nums[left] = nums[right]

count = left + 1
print(nums[:count])
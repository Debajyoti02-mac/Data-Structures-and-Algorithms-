nums = [1, 2, 2, 2, 3, 4, 5]
target = 2


first = -1
last = -1

# Step 1: Find first occurrence
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        first = mid
        right = mid - 1

    elif nums[mid] > target:
        right = mid - 1

    else:
        left = mid + 1


# Step 2: Find last occurrence
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        last = mid
        left = mid + 1

    elif nums[mid] > target:
        right = mid - 1

    else:
        left = mid + 1

print([first, last])
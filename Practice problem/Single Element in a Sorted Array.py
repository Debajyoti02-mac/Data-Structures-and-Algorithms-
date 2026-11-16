
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

left = 0
right = len(nums) - 1

while left < right:
    mid = (left + right) // 2

    # Make mid an even index
    if mid % 2 == 1:
        mid -= 1

    if nums[mid] == nums[mid + 1]:
        # Pair is correct, single element is on the right
        left = mid + 2
    else:
        # Pair is broken, single element is here or on the left
        right = mid

print(nums[left])

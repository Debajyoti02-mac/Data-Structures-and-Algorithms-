
nums = [4, 5, 6, 7, 0, 1, 2]
target = 6

left = 0
right = len(nums) - 1

get_item = -1

while left <= right:
    mid = left + (right - left) // 2

    if nums[mid] == target:
        get_item = mid
        break

    # Left half is sorted
    if nums[left] <= nums[mid]:

        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # Right half is sorted
    else:

        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

print(get_item)

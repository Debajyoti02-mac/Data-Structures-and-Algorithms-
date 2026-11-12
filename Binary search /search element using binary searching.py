nums = [-1, 0, 3, 5, 9, 12]
target = 9

get_item = -1

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        get_item = mid
        break

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

print(get_item)
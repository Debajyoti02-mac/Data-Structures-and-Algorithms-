nums = [7, 2, 5, 10, 8]
k = 2

left = max(nums)  # 10
right = sum(nums)  # 32

while left < right:
    mid = (left + right) // 2

    # Count how many subarrays we need if max sum is `mid`
    subarrays = 1
    current_sum = 0
    for num in nums:
        if current_sum + num <= mid:
            current_sum += num
        else:
            subarrays += 1
            current_sum = num

    if subarrays <= k:
        right = mid  # `mid` works! Try to find a smaller valid limit
    else:
        left = mid + 1  # Too many subarrays needed; `mid` is too small

print(left)  # Output: 18
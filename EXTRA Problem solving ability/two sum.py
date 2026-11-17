nums = [2,7,3,5]
target = 9

def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
  left, right = 0, len(numbers) - 1

  while left < right:
    cal = numbers[left] + numbers[right]
    if cal == target:
      return [left, right]
    elif cal > target:
      right -= 1
    else:
      left += 1
  return []

print(two_sum_sorted(nums, target))



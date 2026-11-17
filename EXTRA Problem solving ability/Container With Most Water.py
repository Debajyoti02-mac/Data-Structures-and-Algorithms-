
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left = 0
right = len(height)-1
max_contains = 0

while left < right:
    contain = min(height[left], height[right]) * (right - left)
    max_contains = max(max_contains, contain)

    if height[left] < height[right]:
      left += 1
    else:
      right -= 1

print(max_contains)

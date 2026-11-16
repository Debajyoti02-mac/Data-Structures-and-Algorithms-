height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left = 0
right = len(height)-1

max_water_can_contain = 0
while left <= right :
    contain = min(height[left], height[right]) * (right - left)
    if height[left] < right:
        left += 1
    else:
        right -= 1
    if contain > max_water_can_contain :
        max_water_can_contain = contain
print(max_water_can_contain)
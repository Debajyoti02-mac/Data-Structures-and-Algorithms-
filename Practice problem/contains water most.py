heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]


left = 0
right = len(heights)-1

area = 0
max_water = 0

while left < right:
    Area = min(heights[left],heights[right])*(right-left)

    if heights[left] < heights[right]:
        left += 1
    else:
        right -= 1
    if Area>max_water:
        max_water = Area
print(f'max_water:{max_water}')



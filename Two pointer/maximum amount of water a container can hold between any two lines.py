#\[Area = \min(h[left],h[right]) \times (right-left)\]

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left = 0 
right = len(heights) - 1 
Area = 0
maximum_water = 0
while left < right :
    Area = min(heights[left],heights[right])*(right-left)
    if heights[left] < heights[right]:
        left+=1
    else:
        right-=1
    if Area > maximum_water :
            maximum_water = Area 
print(maximum_water ) 
            
        
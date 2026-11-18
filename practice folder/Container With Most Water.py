height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

left = 0 
right = len(height)-1
max_quatity = 0 

# until the left became the right 
while left <= right :
    quantity = min(height[right],height[left])*(right-left)
    # if the left is lower than right then increase the left 
    if height[left] < height[right]:
        left +=1
    else:
        right -=1
    if max_quatity < quantity :
        max_quatity = quantity 
print(max_quatity)
        
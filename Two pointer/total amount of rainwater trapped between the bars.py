heights = [4, 2, 0, 3, 2, 5]

left = 0 
right = len(heights)-1

total = 0 

split_length = int(len(heights)/2)

max_left = 0 
max_right = 0 

for i in range(split_length+1):
    if heights[i] > max_left:
        max_left = heights[i]

for i in range(split_length, len(heights)):
    if heights[i] > max_right:
        max_right = heights[i]

for i in range(len(heights)):
    water = min(max_left, max_right) - heights[i]
    if water > 0:
        total += water

print(total)
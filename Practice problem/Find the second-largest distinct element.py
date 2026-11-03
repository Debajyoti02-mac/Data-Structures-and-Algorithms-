nums = [12, 35, 1, 10, 34, 1]

max_element = 0 
second_max = 0 

for i in nums :
    if i > max_element :
        second_max = max_element
        max_element = i
    elif i > second_max and i < max_element :
        second_max = i 
print(second_max)
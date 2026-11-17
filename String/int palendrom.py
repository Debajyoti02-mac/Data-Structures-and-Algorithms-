num = 121
original = num 
reverse = 0 
find = False
while num!= 0 :
    digit = num % 10 
    reverse = reverse * 10 + digit 
    num = num // 10 
    if reverse == original:
        find = True 
    else:
        find = False 
print(find)

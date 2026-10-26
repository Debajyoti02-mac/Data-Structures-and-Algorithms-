nums = [1, 2, 3, 4, 6, 8, 9]
target = 10
seen = []
for i in nums:
    get = target - i 
    
    if get in seen :
        print(get , i)
    seen.append(i)
nums = [3, 8, 4, 6, 2]
target = 10

hash = {}

for i , key  in enumerate(nums):
    get = target - key
    
    if get in hash :
        print(hash[get],i)
    hash[key] = i

        
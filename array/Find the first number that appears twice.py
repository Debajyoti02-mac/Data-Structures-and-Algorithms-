nums = [4, 2, 7, 3, 2, 4, 5]

'''I basically doing that if the value , 
already in seen then break the loop and print the value '''

def first_duplicate(nums):
    count = 0 
    seen = []
    get = 0 
    for i in range(len(nums)):
        if nums[i] in seen :
            count+=1
            get = nums[i]
            break
        else:
            count = 0 

        seen.append(nums[i])
        
    return count,get
print(first_duplicate([4, 2, 7, 3, 2, 4, 5]))
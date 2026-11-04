nums = [5, 3, 4, 1]


""" 
basically their we compare one time one item . 

5 > 3 ---> 3 first 
5 > 4 ----> 4 second 
5 > 1 ---> 1 first replace the area of the all  


"""

for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = key

    print(nums)
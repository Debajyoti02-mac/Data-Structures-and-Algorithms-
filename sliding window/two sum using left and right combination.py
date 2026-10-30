nums = [1, 2, 3, 4, 6, 8, 9]
target = 10

"""
Basically happen in their is , 
we take a empty var that can store the sum while we move both right and left pointers 

Then basically we use a while loop that constently check that the left = 0 < lower than right [the length of the nums]

the sum them = nums[right]+nums[left]
1 + 9 

if sum > target : 10 > 10 : false 
elif sum < target : 10 < 10 : false 
else :
take both result store into result variable together and increment left +1 so left became 2 and right - 1 so it became 8 

"""


left = 0 
right = len(nums)-1
result = []
sum = 0 

while left < right:
    sum = nums[right]+nums[left]
    if sum > target :
        right-=1
    elif sum < target :
        left+=1
    else:
        result.append([nums[right] , nums[left]])
        right-=1
        left+=1
print(result)

    
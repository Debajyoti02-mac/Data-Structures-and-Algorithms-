nums = [0, 1, 0, 3, 12]

array  = []

count = 0
""" 
first i have been check that is the carrying value is zero or not if not zero then append and count for how many values has been stored . 
in next just i have been store after count so it store how many gap has to be filled in the list .. thats it  

 """
# for i in nums:
#     if i!= 0:
#         array.append(i)
#         count = count + 1
# for i in range(count , len(nums)):
#     array.append(0)
# print(array)

pos = 0
for i in range(len(nums)):
    if nums[i]!= 0:
        nums[pos] = nums[i]
        pos+=1
for i in range(pos , len(nums)):
    nums[pos] = 0
    pos += 1
print(nums , count)


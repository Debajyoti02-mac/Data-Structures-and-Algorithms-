
nums = [1, 2, 1, 3, 5, 6, 4]
# # I can do that but why bullshit i need to do that using binary search my chatgpt only know about this ..
# get_index = -1
# max_item = 0
# for i in range(len(nums)):
#     if nums[i] > max_item:
#         get_index = i
#         max_item = nums[i]
# print(get_index , max_item)

left  = 0
right = len(nums) - 1
get_index = -1

while left < right:
    mid = (right + left) // 2

    if nums[mid] < nums[mid+1]:
        left = mid + 1

    else:
        right = mid
print(left)



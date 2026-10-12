nums = [2, 1, 3, 4, 2, 5, 1, 6]
target = 10 

def function(nums,target):
  left = 0 
  right = 0 
  max_length = 0 
  total = 0 
  while right < len(nums):
    total += nums[right]
    while total > target:
      total -=nums[left]
      left+=1 
    if total == target:
      length = right - left + 1
      if max_length < length:
          max_length = length
    right+=1
  return max_length 
          
print(function([2, 1, 3, 4, 2, 5, 1, 6] , 10))

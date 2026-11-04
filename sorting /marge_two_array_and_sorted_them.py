nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8]

i = 0
j = 0
result = [] 

""" 
this sorting is done by two pointer >> 

just take two pointer compare them and add and implement +1 and it grow ups...

"""

while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
        result.append(nums1[i])
        i += 1
    else:
        result.append(nums2[j])
        j += 1

while i < len(nums1):
    result.append(nums1[i])
    i += 1

while j < len(nums2):
    result.append(nums2[j])
    j += 1

print(result)
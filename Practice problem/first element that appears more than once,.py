
# One using simple list : >>
nums = [3, 5, 3, 8, 5, 2, 8, 9]
hash = {}
count= 0 
get_element = 0
seen = []
for i in nums:
    if i in seen :
        count+=1
        get_element = i
        break
    seen.append(i)
print(count , get_element)


# One using hash map >> 
for i in nums:
    if i in hash:
        hash[i]+=1
    else:
        hash[i]=1
for i in nums:
    if hash[i]>1:
        print(i)
        break
nums = [4, 5, 1, 2, 1, 4, 5]
hash = {}

for i in nums:
    if i in hash:
        hash[i]+=1
    else:
        hash[i]=1 
for i in nums:
    if hash[i]==1:
        print(i) 
s = "aabbcde"
hash = {}

for i in s :
    if i in hash :
        hash[i]+=1
    else:
        hash[i] = 1 
for i in s :
    if hash[i]==1 :
        print(i)
        break

        
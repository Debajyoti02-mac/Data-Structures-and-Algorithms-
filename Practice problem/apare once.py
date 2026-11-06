nums = [4, 1, 2, 1, 2 ]

freq = {}
for i in nums:
    if i in freq :
        freq[i]+=1 
    else:
        freq[i]=1 
        
for i in nums:
    if freq[i]==1 :
        print(i)
        break


        
        
nums = [2, 3, 2, 5, 3, 2, 4]

def freq_count(nums):
    freq = {}
    for i in nums:
        if i in freq :
            freq[i]+=1
        else:
            freq[i] = 1 
    return freq 

print(freq_count(nums))

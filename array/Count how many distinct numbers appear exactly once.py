nums = [4, 2, 4, 7, 2, 9, 5, 9, 3]
def fun(nums):
    freq = {}
    count=0
    for i in nums:
        if i in freq:
            freq[i]+=1 
        else:
            freq[i]=1 
    for i , key in freq.items():
        if key == 1 :
            count+=1
        print(count , i)
fun([4, 2, 4, 7, 2, 9, 5, 9, 3])
        
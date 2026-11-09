n = 27
right = n  
left = 0 
answer = 0 

while left <= right :
    mid = (left+right)//2 
    
    if mid * mid == n :
        answer = mid 
    elif mid * mid < n :
        answer = mid 
        left = mid + 1
    else :
        right = mid - 1 
print(f'the nearest squere possible nearest n is : {answer}')
    

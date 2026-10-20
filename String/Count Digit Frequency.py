nums = 122321

def digit(nums):
    count = 0
    while nums > 0 :
        digit = nums % 10 
        if digit == 2:
            count+=1
        nums = nums // 10
    return count 
print(digit(nums))
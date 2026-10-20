num = 12221

'''
digit ----> take the numbers last digit 
reverese ----> thats basically 0 so if digit returns any value then it calculate with 10 * 0 +1 = 1 and this one reverse reserve and then 
after second value come up it multiply with 10 so became 10 * 1 = 10 + digit [2] so became 12 
num automtetically update its own value like // define devide the cut out of the last digit from the number  

'''



def palendrom_num(num):
    original = num 
    reverse = 0 
    while num > 0:
        digit = num % 10 
        reverse = reverse * 10 + digit 
        num = num // 10
    
    if reverse == original :
        return True 
    else:
        return False
print(palendrom_num(num))
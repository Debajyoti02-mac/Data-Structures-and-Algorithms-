num = 121
length = len(str(num))
calculate =  0
original = num 
while num > 0 :
    digit = num % 10 ## return out the last value 
    calculate = calculate + digit ** length  # take the last digit 3 * 3 = 27 + 125 + 1 = 153
    num //= 10 # it basically doing cut out the last element after calculation 
    
if calculate == original :
    print("True")
else:
    print("False")
    
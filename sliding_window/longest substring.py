s = "abcabcbb"

left = 0 
right = 0 
char = ""
max_length =0 
while right < len(s):
    # look at any duplicate is in their then slicing it from left and we increment the left 
    if s[right] in char :

        char = char[1:]

    # after everything outside the if condition add the value one by one so first condition can check it easily 
    # increment the right also 
    char+=s[right]
    # find out the max length based on the max value in that 
    if len(char) >max_length :
        max_length = len(char)
    right+=1

print(max_length)
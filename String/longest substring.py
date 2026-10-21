text = "abcabcbb"

'''
explaination is : 
i used a loop on that based on what ever you want 
then basically take a empty string okay 

then write a condition : if i in char 
if the value already in the string 
string should remove this one by one char[1:] slicing it 
then outside the condtion i used to add all the string value on by one then it check the i in here then cut it . like that 
i got the longest not repeated string value 
'''


def longest_subs(text):
    char = ""
    max_length = 0 
    for i in range(len(text)):
        while text[i] in char :
            char = char[1:]
        char+=text[i]
        
        if max_length < len(char):
            max_length = len(char)
        
    return max_length

print(longest_subs(text))

        
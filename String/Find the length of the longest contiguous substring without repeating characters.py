text = "pwwkew"

def contigious(text):
    count = 0
    max_length = 0
    max_char = ""
    char = ""
    for i in range(len(text)):
        if text[i-1]!=text[i]:
            char+=text[i]
            count+=1 
        else:
            count = 0
            char = ''
        if max_length < count :
            max_length = count 
            max_char = char
            
    return max_length  , max_char
    

print(contigious(text))



    
            
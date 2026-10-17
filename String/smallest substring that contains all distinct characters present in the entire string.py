text = "aabcbcdbca"

def substring(text):
    
    # it store the unique identity 
    char = ""
    min_length = len(text)    
    
    
    
    for i  in text :
        while i in char:
            char = char[1:]
        char+=i 
    
    # if require and len or the output same then return 
    
    if len(char) < min_length:
        min_length = len(char)
        
    return min_length
    
    
print(substring(text))
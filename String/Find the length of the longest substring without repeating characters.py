text = "abcaadbe"

def substring(text):
    char=''
    
    
    for i in text :
        while i in char:
            char = char[1:] 
        char+=i 
    return len(char)

print(substring("abcaadbe"))
        
        
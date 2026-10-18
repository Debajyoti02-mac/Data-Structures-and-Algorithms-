text = "abcabcbb"

def substring(text):
    char = ""
    max_length = 0 
    for i in text :
        if i in char :
            char = char[1:]
        char+=i 
        if max_length < len(char) :
            max_length = len(char)
    return max_length

print(substring(text))
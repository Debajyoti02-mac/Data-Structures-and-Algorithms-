text = "aabbbbccddddddaa"

def frequent(text):
    count = 1
    max_count = 1
    char = text[0]
    for i in range(1,len(text)):
        if text[i-1] == text[i]:
            count+=1 
        else:
            count = 1 
        if count > max_count :
            max_count = count 
            char = text[i]
    return max_count , char

print(frequent(text))

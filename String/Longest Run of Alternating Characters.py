text = "aabbabab" 

# Longest alternetive 

def alternetive(text):
    count = 1
    max_count = 0 
    for i in range(1,len(text)):
        if text[i-1]!=text[i]:
            count+=1 
            
        else:
            count = 1
        if max_count < count :
            max_count = count
    return max_count 

print(alternetive(text))
text = "banana" 

def freq_count(text):
    max_count = 1
    freq ={}
    max_char = ""
    
    for i in text :
        if i in freq:
            freq[i]+=1 
        else:
            freq[i]=1 
    for i in text :
        if max_count < freq[i]:
            max_count = freq[i]
            max_char = i 
    return max_count , max_char
print(freq_count(text=text))
    
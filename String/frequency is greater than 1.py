text = "aabbccdde"

def frequency(text):
    
    seen = set()
    for i in text:
        if i in seen :
            return i 
        seen.add(i)
        
print(frequency(text))
        
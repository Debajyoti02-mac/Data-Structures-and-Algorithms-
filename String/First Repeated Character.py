text = "abcaefb"

def repeated(text):
    seen = set()
    
    for i in text :
        if i in seen :
            return i 
        seen.add(i)
        
print(repeated(text))
text = "programming"

def unique(text):
    seen = ''
    for i in text :
        if i not in seen :
            seen+=i
    return len(seen) 

print(unique(text))
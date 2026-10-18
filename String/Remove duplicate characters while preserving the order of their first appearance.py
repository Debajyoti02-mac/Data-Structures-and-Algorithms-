text = "programming"

def duplicate_remove(text):
    seen = ""
    for i in text :
        if i not in seen :
            seen+=i
    return seen 
print(duplicate_remove(text))
    
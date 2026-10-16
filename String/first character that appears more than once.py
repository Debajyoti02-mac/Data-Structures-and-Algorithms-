text = "programming"

def appears(text):
    sets = set()

    for i in text:
        if i  in sets :
            return i 
        sets.add(i)
            
    return "No two times repeated value " 
                    
print(appears("programming"))
        
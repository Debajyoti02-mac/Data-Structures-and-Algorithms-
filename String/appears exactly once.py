text = "aabbcddee"

def appare(text):
    hash = {}
    for i in text:
        if i in hash :
            hash[i]+=1 
        else:
            hash[i]=1 
            
    for i in text :
        if hash[i]==1:
            return i 
    return "No char is repeated exactly one time"
    
print(appare(text))
text = "levelheaded"

def fun(text):
    hash = {}
    for i in text:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1 
    for i in text:
        if hash[i]==1:
            return i 
    
print(fun("levelheaded"))
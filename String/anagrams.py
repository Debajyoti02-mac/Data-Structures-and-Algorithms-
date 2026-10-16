
def anagrams():
    s1 = "listen"
    s2 = "silent"
    
    hash1 = {}
    hash2 = {}
    
    if len(s1) == len(s2):
        for i in s1 :
            if i in hash1:
                hash1[i]+=1 
            else:
                hash1[i]=1 
        for i in s2:
            if i in hash2:
                hash2[i]+=1 
            else:
                hash2[i]=1
    
        if hash1 == hash2:
            return True 
    return False
        

print(anagrams())
        
        
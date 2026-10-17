text = "swiss"

def freq_count(text):
    seen = {}
    for i in text:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1 
    for i in text :
        if seen[i]==1:
            return i 
    
    return "No that like char valid in the string that apare exact once"

print(freq_count(text))
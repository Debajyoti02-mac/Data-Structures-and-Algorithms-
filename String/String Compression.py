text = "aaabbccccdaa"
hash = {}

char = ""
count = 1
max_count = 1

for i in range(1,len(text)):
    if text[i] == text[i-1]:
        count+=1 
        
        
    else:
        char+=text[i-1]+str(count)
        count=1
        
    if max_count < count :
        max_count = count 
char += text[-1] + str(count)
        
print(char , max_count)
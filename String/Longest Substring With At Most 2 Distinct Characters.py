text = "eceba"

# The length return should be more than 2 
char = ''
max_length = 0 
left = len(text)-1
for i in text :
    char+=i
        
    while len(set(char)) > 2 :
        char = char[1:]
    if max_length < len(char) :
        max_length = len(char)
    
print('this is char ',max_length )

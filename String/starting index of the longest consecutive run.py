text = "aabcccddddcc"

def index(text):
    count = 1 
    max_count = 0
    index = 0 
    for i in range(1,len(text)):
        if text[i]==text[i-1]:
            count+=1 
        else:
            count = 1 
            
        if max_count < count :
            ''' the idea behind this logic is if the index return where ends then basically do that 
            i = 9 
            count --> total count number in the longest contigious is 4 
            so it returns 5 
            
            but in count we aparely addded one is so + 1 
            so it returns 5 + 1 = 6
            '''
            index = i-count+1
            max_count = count
            
    return max_count , index 

print(index(text))
            
        
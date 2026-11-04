s = "listen"
t = "silent"

freq1={}
freq2={}

if len(s) == len(t):
    for i in s :
        if i in freq1 :
            freq1[i] +=1
        else:
            freq1[i] = 1 
    for i in t :
        if i in freq2 :
            freq2[i] +=1
        else:
            freq2[i] = 1 
    if freq1 == freq2 :
        print(True)
    else: print(False)
else: print(False)
            

        
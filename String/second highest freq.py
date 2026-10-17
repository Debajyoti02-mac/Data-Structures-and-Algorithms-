text = "mississippi"
most_freq = 0 
second_most = 0 
    
second_repeat_char = ""

hash = {}
for i in text :
    if i in hash:
        hash[i]+=1 
    else:
        hash[i]=1 

for key , value in hash.items():
  if most_freq < value :
    second_most = most_freq
    most_freq = value

  elif value < most_freq and value > second_most:
    second_most = value 
    second_repeat_char = key

    
print(second_most , second_repeat_char)
  
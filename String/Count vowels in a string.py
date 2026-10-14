text = "programming is amazing"

def fun(text):
    vowels = 'AIOUEaioue'
    count = [i for i in  text if i in vowels]
    total_vowels = 0 
    for i in count :
        total_vowels+=1
    return total_vowels 
print(fun("programming is amazing"))


text = "hello programming"

def fun(text):
    hash = {}
    for i in text:
        if i != " ":
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
    return hash

print(fun("hello programming"))
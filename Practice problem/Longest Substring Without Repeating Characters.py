s = "dvdf"
left = 0

char = ""
for i in s:
    if i in char:
        char = char[1:]
    char+=i

print(len(char))
words = ["flower", "flow", "flight"]
prefix = ""

for i in range(len(words[0])):
    Match = True
    for j in range(len(words)):
        if i >= len(words[j]):
            break
        if words[j][i] != words[0][i]:
            Match = False
            break
    if not Match:
        break
    prefix+=words[0][i]
        
print(prefix)
    
s = "abcabcbb"
char = ""
max_length = 0
seen = set()
left = 0

for i in range(len(s)):
    if s[i] in seen:
        seen.remove(s[left])
        left+=1
    seen.add(s[i])
    max_length = max(max_length, i - left + 1)
print(max_length)


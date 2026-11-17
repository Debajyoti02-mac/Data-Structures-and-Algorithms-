s = "racecar"
left = 0
right = len(s) - 1

find = True

while left < right:
    if s[left] != s[right]:
        find = False
        break

    left += 1
    right -= 1

print(find)
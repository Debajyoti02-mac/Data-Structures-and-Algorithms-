s = "A man, a plan, a canal: Panama"

# Step 1: Clean the string
s = ''.join(char.lower() for char in s if char.isalnum())

# Step 2: Initialize pointers
left = 0
right = len(s) - 1

# Step 3: Compare characters
while left < right:
    if s[left] != s[right]:
        print(False)
        break

    left += 1
    right -= 1

else:
    print(True)
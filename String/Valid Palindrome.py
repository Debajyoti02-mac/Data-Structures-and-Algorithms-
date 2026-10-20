text = "A man, a plan, a canal: Panama"

def palindrome(text):
    text = text.lower()
    clean = ""

    for i in text:
        if i.isalnum():
            clean += i

    char = ""
    right = len(clean) - 1

    for i in range(len(clean)):
        char += clean[right]
        right -= 1

    return char == clean

print(palindrome(text))
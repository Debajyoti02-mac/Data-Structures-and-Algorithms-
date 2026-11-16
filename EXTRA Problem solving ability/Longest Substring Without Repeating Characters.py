s = "abcabcbb"
def longest_substring(s):
    char = ""
    max_length = 0
    val  = ""

    for i in s:
        if i  in char :
            char = char[1:]
        char += i
        if max_length < len(char) :
            max_length = len(char)
            val = char
    return max_length  , val

print(longest_substring(s))


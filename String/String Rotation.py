s1 = "waterbottle"
s2 = "erbottlewat"

def rotation(s1,s2):
    combine = s1 + s1 
    return len(s1) == len(s2) and s2 in combine 

print(rotation(s1,s2))
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
v = c = w = q = 0

s = input("Enter string: ")
for i in s.lower():
    if i in vowels:
        v += 1
    elif i in consonants:
        c += 1
    elif i == "?":
        q += 1

s_split = s.split()
w = len(s_split)

print("Vowels:",v,"\nConsonants:",c,"\nWords:",w,"\nQuestion Marks:",q)    
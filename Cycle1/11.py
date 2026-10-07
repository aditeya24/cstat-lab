filename = input("Enter the file name: ")

with open(filename, "r") as file:
    text = file.read()

words = len(text.split())

sentences = 0
for ch in text:
    if ch in ".!?":
        sentences += 1

uppercase = 0
lowercase = 0
special = 0

for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif not ch.isdigit() and not ch.isspace():
        special += 1


print("Words:", words)
print("Sentences:", sentences)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Symbols:", special)

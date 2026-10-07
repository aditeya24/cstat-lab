def is_valid(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0



s = input("Enter the bracket string: ")

if is_valid(s):
    print("Valid")
else:
    print("Invalid")

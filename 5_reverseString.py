def reverseString(S):
    stack = []
    for char in S:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string

S = "GeeksforGeeks"
reversed_S = reverseString(S)
print(reversed_S)  # Output: skeeGrofskeeG

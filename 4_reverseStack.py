def reverseStack(stack):
    if len(stack) <= 1:
        return

    top = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack, top)


def insertAtBottom(stack, element):
    if len(stack) == 0:
        stack.append(element)
        return

    top = stack.pop()
    insertAtBottom(stack, element)
    stack.append(top)


stack1 = [3, 2, 1, 7, 6]
reverseStack(stack1)
print(stack1)  # Output: [6, 7, 1, 2, 3]

stack2 = [4, 3, 9, 6]
reverseStack(stack2)
print(stack2)  # Output: [6, 9, 3, 4]

def evaluatePostfixExpression(S):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in S:
        if char not in operators:
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack.pop()


S1 = "231*+9-"
result1 = evaluatePostfixExpression(S1)
print(result1)  # Output: -4

S2 = "123+*8-"
result2 = evaluatePostfixExpression(S2)
print(result2)  # Output: -3

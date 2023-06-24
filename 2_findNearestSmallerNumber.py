def findNearestSmallerNumber(a):
    n = len(a)
    stack = []
    result = [-1] * n

    for i in range(n):
        while stack and stack[-1] >= a[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(a[i])

    return result

a1 = [1, 6, 2]
result1 = findNearestSmallerNumber(a1)
print(result1)  # Output: [-1, 1, 1]

a2 = [1, 5, 0, 3, 4, 5]
result2 = findNearestSmallerNumber(a2)
print(result2)  # Output: [-1, 1, -1, 0, 3, 4]

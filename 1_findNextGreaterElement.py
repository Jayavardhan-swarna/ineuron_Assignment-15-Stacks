def findNextGreaterElement(arr):
    N = len(arr)
    stack = []
    result = [-1] * N

    for i in range(N):
        while stack and arr[stack[-1]] < arr[i]:
            top_element_index = stack.pop()
            result[top_element_index] = arr[i]
        stack.append(i)

    while stack:
        remaining_elements_index = stack.pop()
        result[remaining_elements_index] = -1

    return result


arr = [1, 3, 2, 4]
result = findNextGreaterElement(arr)
print(result)  # Output: [3, 4, 4, -1]

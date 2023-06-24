class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if not self.q1 and not self.q2:
            return -1

        if not self.q2:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            return self.q1.pop(0)

        return self.q2.pop(0)

    def top(self):
        if not self.q1 and not self.q2:
            return -1

        if not self.q2:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            return self.q1[0]

        return self.q2[0]



stack1 = Stack()
stack1.push(2)
stack1.push(3)
print(stack1.pop())  # Output: 3
stack1.push(4)
print(stack1.pop())  # Output: 4

stack2 = Stack()
stack2.push(2)
print(stack2.pop())  # Output: 2
print(stack2.pop())  # Output: -1
stack2.push(3)
print(stack2.top())  # Output: 3

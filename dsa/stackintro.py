from collections import deque
stack=deque()
stack.append('madhu')
stack.append('gagan')
stack.append('seeta')
stack.append('rohan')
print(stack)
stack.pop()
print(stack)
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)

s=Stack()
s.push(5)
print(s.peek())
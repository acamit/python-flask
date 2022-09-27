# stack = []
#
# stack.append('a')
# stack.append('b')
# stack.append('c')
#
# print(stack)
#
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
#
# print(stack)

from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print(stack)

print(stack.pop())

print(stack.pop())
print(stack.pop())

print(stack)
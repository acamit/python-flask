from queue import LifoQueue

stack = LifoQueue()
# get size of queue
print(stack.qsize())

stack.put('a')
stack.put('b')
stack.put('c')

print(f'full : {stack.full()}')
print(stack.qsize())

print(stack.get())
print(f'full : {stack.full()}')
print(f'is empty {stack.empty()}')

print(stack.get())
print(stack.get())

print(f'is empty {stack.empty()}')

from queue import LifoQueue


class SpecialStack:
    def __init__(self):
        self.stack = LifoQueue()
        self.minStack = LifoQueue()

    def push(self, x):
        if self.stack.empty():
            self.stack.put(x)
            self.minStack.put(x)

        else:
            self.stack.put(x)
            y = self.minStack.get(block=False)
            if x < y:
                self.minStack.put(x)
            else:
                self.minStack.put(y)

    def pop(self):
        x = self.stack.get()
        self.minStack.get()
        return x

    def getmin(self):
        x = self.minStack.get()
        self.minStack.put(x)  # just returning current minimum. not deleting it.
        return x


if __name__ == '__main__':
    s = SpecialStack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.getmin())
    s.push(5)
    print(s.getmin())

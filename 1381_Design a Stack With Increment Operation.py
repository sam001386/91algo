class CustomStack(object):
    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k, val):
        index = 0
        if self.stack:
            while index <= len(self.stack) - 1 and k > 0:
                self.stack[index] += val
                k -= 1 
                index += 1 

'''
    60ms, faster than 70.66% of python sols
    17.8mb, less than 80.39% of python sols
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.l = 0
        self.m = 0
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.l += 1
        if self.l == 1:
            self.m = x
        elif x < self.m:
            self.m = x

    def pop(self) -> None:
        r = self.stack.pop()
        self.l -= 1
        if r == self.m:
            if self.l > 0:
                minv = self.stack[0]
                for i in self.stack:
                    if i < minv:
                        minv = i
                self.m = minv
        return r

    def top(self) -> int:
        return self.stack[self.l-1]

    def getMin(self) -> int:
        return self.m


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

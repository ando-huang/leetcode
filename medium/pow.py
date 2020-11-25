'''
    28ms, faster than 76.94% of python3 sols
    14.3MB, less than 9.00% of python3 sols
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2 == 1:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

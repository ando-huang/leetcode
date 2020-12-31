'''
    32ms, faster than 40.72% of python sols
    14.3MB, less than 25.735 of python sols
'''

class Solution:
    def findNthDigit(self, n: int) -> int:
        n -= 1
        for i in range(1, 11):
            first = 10**(i - 1)
            if n < 9 * first * i:
                return int(str(first + n/i)[n%i])
            n -= 9 * first * i

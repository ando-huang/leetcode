'''
    36ms, faster than 32.13% of python sols
    14.2MB, less than 59.53% of python sols
'''

class Solution:
    def addDigits(self, num: int) -> int:
        final = num
        while final > 9:
            s = 0
            while final > 0:
                s += final % 10
                final //= 10
            final = s
        return final

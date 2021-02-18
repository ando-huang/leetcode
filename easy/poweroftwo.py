'''
    32ms, faster than 69.03% of python sols
    14.1MB, less than 90.34% of python sols
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while(n > 1):
            if n % 2== 0:
                n/=2
                continue
            return False
        return True

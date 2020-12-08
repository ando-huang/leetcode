'''
    40ms, faster than 5.38% of python3 sols
    14.4MB, less than 17.22% of python sols
'''

class Solution:
    def reverse(self, x: int) -> int:
        
        def divide(number, divider):
            return int(number / divider)
        
        def mod(number, m):
            if number < 0:
                return number % -m
            return number % m
        
        MAX_INT = 2 ** 31 - 1 # 2147483647
        MIN_INT = -2 ** 31    #-2147483648
        
        res = 0
        while x:
            pop = mod(x, 10)
            x = divide(x, 10)
            if res > divide(MAX_INT, 10) or (res == divide(MAX_INT, 10) and pop > 7):
                return 0
            if res < divide(MIN_INT, 10) or (res == divide(MAX_INT, 10) and pop < -8):
                return 0
            res = res * 10 + pop
            
        return res

'''
    24ms faster than 96.20% of python3 sols
    14.2mb less than 17.78% of python3 sols
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] += 1
        return digitsend = len(digits) -1
        digits[end] += 1
        while(digits[end] == 10):
            digits[end] = 0
            end -= 1
            if end == -1:
                digits.insert(0, 1)
                break
            digits[end] += 1
        return digits

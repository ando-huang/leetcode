'''
    156ms faster than 8.49% of python sols
    21.5MB, less than 18.97% of python sols
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        used = {}
        for i in nums:
            if i in used:
                return True
            used[i] = 1
        return False

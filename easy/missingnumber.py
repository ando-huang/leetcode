'''
    148ms, faster than 24.49% of python sols
    15.4MB, less than 66.43% of python sols
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        expected = 0
        
        for i in nums:
            if i == expected:
                expected += 1
            elif i > expected:
                return expected
        return len(nums)


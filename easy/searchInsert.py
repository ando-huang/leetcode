'''
    faster than 48% of python sols
    less space than 10% of python sols
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ind = 0
        while ind < len(nums):
            if nums[ind] < target:
                ind += 1
            else:
                return ind
        return len(nums)

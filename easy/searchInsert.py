'''
    48ms faster than 63% of python sols
    14.8MB less than 20% of python sols
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

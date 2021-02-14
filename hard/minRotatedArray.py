'''
    python is SOOOO difficult

    52ms, faster than 72.00% of python sols
    14.9mb, less than 47.76% of python sols
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]

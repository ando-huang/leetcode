'''
    kind of a braindead solution but it worked

    36ms, faster than 90.82% of python sols
    14.7mb, less than 32.06% of python sols
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]

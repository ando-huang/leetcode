'''
    56ms, faster than 96.26% of python sols
    15.1Mb, less than 41.88% of python sols
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]

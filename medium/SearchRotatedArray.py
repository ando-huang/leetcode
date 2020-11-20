'''
    36ms, faster than 85.78% of python sols
    14.6MB, less than 9.99% of python sols
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

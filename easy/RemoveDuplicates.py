'''
    92ms, faster than 34.12% of python sols
    15.7MB, less than 62.84% of python sols
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        curr = nums[0]
        i = 1
        while (i < len(nums)):
            if nums[i] == curr:
                nums.pop(i)
            else:
                curr = nums[i]
        return len(nums)

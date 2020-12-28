'''
    56ms, faster than 69.48% of python sols
    15.7MB, less than 70.74% of python sols
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 2
        while(i < len(nums)):
            if nums[i-2] != nums[i]:
                return nums[i-2]
            i += 3
        return nums[len(nums)-1]

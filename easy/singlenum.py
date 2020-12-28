'''
    120ms, faster than 96.81% of python sols
    16.7MB, less than 14.60% of python sols
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        i = 1
        while(i < len(nums)):
            if nums[i] != nums[i-1]:
                return nums[i-1]
            i += 2
        return nums[len(nums)-1]    
        

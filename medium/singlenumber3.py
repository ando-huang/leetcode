'''
    64ms, faster than 30.30% of python sols
    15.8mb, less than 53.80% of python sols
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ret = []
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i-1] != nums[i]:
                ret.append(nums[i-1])
                if len(ret) == 2:
                    return ret
                i += 1
            else:
                i += 2
        ret.append(nums[len(nums)-1])
        return ret

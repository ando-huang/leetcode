class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        expected = 1
        while i < len(nums):
            if nums[i] <= 0:
                i+=1
            else:
                break
        
        curr = 0
        while i < len(nums):
            if nums[i] == curr:
                i += 1
                continue
            if nums[i] != expected:
                return expected
            expected += 1
            i += 1
            curr = nums[i]
        return expected + 1


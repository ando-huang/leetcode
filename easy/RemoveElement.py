'''
    36ms, faster than 25.19% of python sols
    13.9MB, less than 93.56% of python sols

'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        finallen = len(nums)
        i = 0
        while i < finallen:
            if nums[i] == val:
                nums.pop(i)
                finallen -= 1
            else:
                i += 1
        return finallen

'''
    120ms, faster than 9.68% of python sols
    21.7MB, less than 60.96% of python sols
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            d[v] = i
        return False

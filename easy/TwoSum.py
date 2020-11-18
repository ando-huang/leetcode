#mediocre runtime and memory usage, but it works

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        parsed = {}
        for i in range(len(nums)):
            if (target - nums[i]) in parsed:
                return [parsed[target-nums[i]], i]
            else:
                parsed[nums[i]] = i


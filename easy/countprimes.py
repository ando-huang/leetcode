class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [i for i in range(2, n)]
        primecount = 0
        for i in range(len(nums)/2):
            if nums[i] != -1:
                for j in range(i*2, len(nums)):
                    nums[j] = -1
                primecount += 1
        for i in range(len(nums)/2, len(nums)):
            if nums[i] != -1:
                primecount += 1
                
        return primecount

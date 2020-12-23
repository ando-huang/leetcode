class Solution:
    '''
        88ms, faster than 33.50% of python sols
        15.6MB, less than 6.50% of python sols
        This solution attempts to use binary search to get initial index
        theoretically better but its really bad, perhaps due to implementation
    '''
    class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = -1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                i = mid
                break
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        
        if i == -1:
            return [-1, -1]

        iL, iH = i, i
        while iL > 0:
            if nums[iL-1] == target:
                iL -= 1
            else:
                break
        while iH < len(nums)-1:
            if nums[iH+1] == target:
                iH += 1
            else:
                break
        return [iL, iH]


    '''
        84ms, faster than 63.91% of python sols
        15.2MB, less than 61.21% of python sols
        THIS IS AN ITERATIVE BRUTE FORCE solution
    '''
    def searchRangeITER(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
                
        return [first, last]        

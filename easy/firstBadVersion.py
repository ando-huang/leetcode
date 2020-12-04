'''
    28ms, faster than 68.49% of python sols
    14.1MB, less than 38.90% of python sols
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        mid = int((left+right)/2)
    
        if isBadVersion(n) == False:
            mid = None
        else:
            while right - left > 1:
            
                if isBadVersion(mid):
                    right = mid
                    mid = int((left+right)/2)
                else:
                    left = mid
                    mid = int((left+right)/2)
                
            if right - left == 1 and isBadVersion(left):
                mid = left
            else:
                mid = right
               
        return mid

'''
    the nested while probably makes it worse
    52ms, faster than 6% of python sols
    14.5MB, less than 12% of python sols

'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        n1elems = 0
        
        while p1 < m + n and p2 < n:
            if n1elems == m:
                break
            if nums1[p1] > nums2[p2]:
                t = nums1[p1]
                nums1[p1] = nums2[p2]
                tp = p1
                while(tp < m+n-1):
                    t2 = nums1[tp+1]
                    nums1[tp+1] = t
                    t = t2
                    tp += 1
                p1 += 1
                p2 += 1
            else:
                p1 += 1
                n1elems+=1
        
        while(p2 < n):
            nums1[p1] = nums2[p2]
            p1 += 1
            p2 += 1

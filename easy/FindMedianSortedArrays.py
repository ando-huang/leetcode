'''
    92ms, faster than 58.91% of other Python subs
    14.4MB, less than 32.32% of other Python subs
'''

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        c1 = 0
        c2 = 0
        while(c1 < len(nums1) and c2 < len(nums2)):
            if(nums1[c1] < nums2[c2]):
                nums3.append(nums1[c1])
                c1 += 1
            else:
                nums3.append(nums2[c2])
                c2 += 1
    
        while(c1 < len(nums1)):
            nums3.append(nums1[c1])
            c1+=1
        while(c2 < len(nums2)):
            nums3.append(nums2[c2])
            c2+=1
        
        if len(nums3) % 2 == 0:
            m = nums3[len(nums3)//2] + nums3[len(nums3)//2 - 1]
            m /= 2
            return m
        else:
            return float(nums3[len(nums3)//2])

'''
    24ms, faster than 97.82% of python sols
    14.2MB, less than 77.82% of python sols
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l = list(t)
        l.sort()
        s2 = list(s)
        s2.sort()
        for i in range(len(s2)):
            if l[i] != s2[i]:
                return l[i]
        return l[len(l)-1]

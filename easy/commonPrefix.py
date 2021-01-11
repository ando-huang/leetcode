'''
    36ms, faster than 52.6% of python sols
    14.4MB, less than 51.18% of python sols
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for s in strs:
                if s[i] != ch:
                    return shortest[:i]
        return shortest 

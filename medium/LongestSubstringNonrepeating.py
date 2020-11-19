'''
    2064ms, faster than 5.01% of python sols
    14.2MB, less than 77.27% of python sols
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengths = [1 for i in range(len(s))]
        for i in range(len(s)):
            used = []
            count = 0
            for j in range(i, len(s)):
                if s[j] in used:
                    break
                else:
                    used.append(s[j])
                    count += 1
            lengths[i] = count
        
        n = 0
        for i in lengths:
            if i > n:
                n = i
        return n
    

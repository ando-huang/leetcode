'''
    32ms, faster than 51.71% of python sols
    14.1MB, less than 87.03% of python sols
'''

class Solution:
    def checkRecord(self, s: str) -> bool:
        lcount = 0
        acount = 0
        for day in s:
            if day == 'A':
                acount += 1
            if day == 'L':
                if lcount == 2:
                    return False
                lcount += 1
            else:
                lcount = 0
        if acount > 1:
            return False
        return True

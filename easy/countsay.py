'''
    40ms, faster than 85.41% of python sols
    14.4MB, less than 18.23% of python sols
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l
                    count = 1
            temp += str(count)+let
            s = temp
        return s

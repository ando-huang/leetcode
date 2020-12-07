class Solution:
    def solve(self, s):
        dict = {}
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i] = 1
        
        singlectr = 0
        for count in dict.values():
            if count%2 == 1:
                singlectr += 1
        return singlectr <= 1

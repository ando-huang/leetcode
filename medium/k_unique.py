class Solution:
    def solve(self, s, k):
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i]= 1
                
        count = 0
        if len(d) < k:
            return 0
        
        while(len(d) != k):
            min_key = min(d, key=d.get)
            count += d[min_key]
            del d[min_key]
        
        return count

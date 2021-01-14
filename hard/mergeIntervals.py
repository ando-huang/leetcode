class Solution:
    def solve(self, intervals, target):
        if len(intervals) == 0:
            intervals.append(target)
            return intervals
        
        i = 0
        while i < len(intervals) and intervals[i][0] < target[0]:
            i += 1
        if i > 0:
            i -= 1
        
        j = i
        while j < len(intervals) and intervals[j][0] < target[1]:
            j+= 1
        
        newInt = [intervals[i][0], intervals[j-1][1]]

        for k in range(j-i -1):
            intervals.pop(i)
        intervals[i] = newInt

        return intervals


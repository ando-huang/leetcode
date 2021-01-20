'''
    INCOMPLETE SOL, missing some edge cases

'''

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
    
    def solve2(self, intervals, target):
        newInt = [-1, -1]
        if intervals[0][0] < target[0]:
            newInt[0] = target[0]
        max = len(intervals)-1
        i = 0
        while i <= max and intervals[i][1] < target[0]:
            i += 1
        j = i
        while j <= max and intervals[i][0] < target[1]:
            j += 1 

        return intervals
        
    def solve3(self, intervals, target):
        newInt = []
        for i in range(len(intervals)):
            if target[0] > intervals[i][0]:
                newInt.append(intervals[i])
            elif target[1] < intervals[i][1]:
                return newInt + [target] + intervals[i:]
            else:
                target[0] = min(target[0], intervals[i][0])
                target[1] = max(target[1], intervals[i][1])

        return newInt + [target]

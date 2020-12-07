from collections import deque

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root == None:
            return -1
        minSum = root.val
        q = deque()
        q.append(root)
        minlvl = 0
        currlvl = 0
        
        while(len(q) > 0):
            lvllen = len(q)
            currSum = 0
            while(lvllen > 0):
                curr = q.popleft()
                currSum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                lvllen -=1
            if minSum > currSum:
                minSum = currSum
                minlvl = currlvl
            currlvl += 1
        return minlvl

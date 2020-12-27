'''
    52ms, faster than 55.95% of python sols
    16MB, less than 41.13% of python sols
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(root, ls):
            if root != None:
                for i in root.children:
                    dfs(i, ls)
                ls.append(root.val)
        l = []
        dfs(root, l)
        return l

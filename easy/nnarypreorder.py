'''
    52ms faster than 57.57% of python sols
    16.1mb less than 41.45% of python sols
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root, lst):
            if root != None:
                lst.append(root.val)
                for child in root.children:
                    dfs(child, lst)
        l = []
        dfs(root, l)
        return l

'''
    40ms, faster than 5.61% of python sols
    14.1MB, less than 84.3% of python sols
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node, lst):
            if node != None:
                lst.append(node.val)
                dfs(node.left, lst)
                dfs(node.right, lst)
        l = []
        dfs(root, l)
        return l
    
        

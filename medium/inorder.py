'''
    40ms, faster than 5.37% of python sols
    14.4MB, less than 8.85% of python sols
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def idfs(node, lst):
            if node != None:
                idfs(node.left, lst)
                lst.append(node.val)
                idfs(node.right, lst)
        l = []
        idfs(root, l)
        return l

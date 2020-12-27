'''
    44ms, faster than 7.38% of python sols
    14.4MB, less than 8.10% of python sols
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def pdfs(root, lst):
            if root != None:
                pdfs(root.left, lst)
                pdfs(root.right, lst)
                lst.append(root.val)
        l = []
        pdfs(root, l)
        return l

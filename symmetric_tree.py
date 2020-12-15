'''
    36ms faster than 52.22% of python sols
    14.5MB less than 19.19% of python sols
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        def samechild(left, right):
            if left is None and right is None:
                return True
            if left is not None and right is not None:
                if left.val == right.val:
                    return (samechild(left.left, right.right) and samechild(left.right, right.left))
        return samechild(root.left, root.right)

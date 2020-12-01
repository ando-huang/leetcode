# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def solve(self, root):
        return self.wrap( root, 0)
        
    def wrap(self, node, val):
        if node == None:
            return 0
        currval = 10*val + node.val
        if node.left == None and node.right == None:
            return currval
        return (self.wrap(node.left, currval) + self.wrap(node.right, currval))
    

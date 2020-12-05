'''
    3ms, faster than 100% of python sols
    0 external space
'''

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        head = node
        if node == None:
            return node
        curr = node
        while(curr and curr.next):
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next
        return head
            

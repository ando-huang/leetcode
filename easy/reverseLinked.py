'''
    40ms, faster than 38.81% of python sols
    15.4MB, less than 99.55% of python sols
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        r = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = r
            r = curr
            curr = temp
        return r

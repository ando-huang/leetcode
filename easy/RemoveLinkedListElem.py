'''
    68ms, faster than 68.67% of python sols
    17.1MB, less than 9.56% of python sols
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        
        deadhead = ListNode(-1)
        deadhead.next = head
        curr = deadhead
        while(curr.next != None):
            if(curr.next.val == val):
                curr.next = curr.next.next
            else:
                curr = curr.next
        return deadhead.next
        

        

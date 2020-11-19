'''
    40ms, faster than 39.06% of python sols
    14.1MB, less than 73.06% of python sols
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        l3 = ListNode()
        if(l1.val < l2.val):
            l3.val = l1.val
            l1 = l1.next
        else:
            l3.val = l2.val
            l2 = l2.next
        curr = l3
        while(l1!= None and l2 != None):
            newN = ListNode()
            if(l1.val < l2.val):
                newN.val = l1.val
                l1 = l1.next
                
            else:
                newN.val = l2.val
                l2 = l2.next
            curr.next = newN
            curr = curr.next

        if l1 != None:
            curr.next = l1
        if l2 != None:
            curr.next = l2

        return l3

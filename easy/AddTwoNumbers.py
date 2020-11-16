# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head

        carryOver = 0
        while(l1 != None and l2 != None):
            cSum = l1.val + l2.val + carryOver
            if cSum >= 10:
                carryOver = 1
                cSum -= 10
            else:
                carryOver = 0
            newN = ListNode(cSum)
            curr.next = newN
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while(l1 != None):
            cSum = l1.val + carryOver
            if cSum >= 10:
                carryOver = 1
                cSum -= 10
            else:
                carryOver = 0
            newN = ListNode(cSum)
            curr.next = newN
            curr = curr.next
            l1 = l1.next
        while(l2 != None):
            cSum = l2.val + carryOver
            if cSum >= 10:
                carryOver = 1
                cSum -= 10
            else:
                carryOver = 0
            newN = ListNode(cSum)
            curr.next = newN
            curr = curr.next
            l2 = l2.next

        return head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        curr = head
        while(curr.next != None and k >= 0):
            curr = curr.next
        temp = head
        head = curr.next
        curr.next = None
        c2 = head
        while c2.next != None:
            c2 = c2.next
        c2.next = temp
        return head
    def rotateRight2(self, head: ListNode, k: int)-> ListNode:
        '''
    32ms, faster than 92.37% of python sols
    14.4MB, less than 30.87% of python sols
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        lastElement = head
        length = 1
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1
        k = k % length

        lastElement.next = head

        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next

        answer = tempNode.next
        tempNode.next = None

        return answer

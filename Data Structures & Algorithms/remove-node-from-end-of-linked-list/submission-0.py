# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        n = length - n
        prev = None
        curr = head
        i = 0
        for i in range(i, n):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        else:
            head = head.next

        return head

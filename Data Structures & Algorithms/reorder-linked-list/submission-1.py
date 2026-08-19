# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = slow
        slow = slow.next
        prev.next = None
        slow = self.reverseList(slow)
        
        while slow:
            nxtA = head.next
            nxtB = slow.next

            head.next = slow
            head.next.next = nxtA
            slow = nxtB
            head = head.next.next



    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

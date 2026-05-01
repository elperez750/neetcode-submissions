# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        p1 = None
        p2 = head

        while p2:
            current = current.next

            p2.next = p1
            p1 = p2
            p2 = current

        head = p1
        return head



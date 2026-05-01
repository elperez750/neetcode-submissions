# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head

        new_head = self.reverseList(head.next)

        # Fix the pointers
        head.next.next = head  # Make the next node point back to the current node
        head.next = None  # Break the forward link to avoid a cycle

        # Return the new head of the reversed list
        return new_head

        return head
       
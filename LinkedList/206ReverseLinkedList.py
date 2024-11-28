# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return head

        prev = None
        curr = head

        while(curr is not None):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        # due to the while statement and termination, you return prev, not curr
        return prev

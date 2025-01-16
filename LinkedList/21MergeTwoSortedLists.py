# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        h1 = list1
        h2 = list2
        list3 = None

        # base case
        if(h1 != None and h2!= None):
            if(h1.val < h2.val):
                list3 = ListNode(h1.val, next=None)
                h1 = h1.next
            else:
                list3 = ListNode(h2.val, next=None)
                h2 = h2.next
        elif h1 != None:
            list3 = ListNode(h1.val, next=None)
            h1 = h1.next
        elif h2 != None:
            list3 = ListNode(h2.val, next=None)
            h2 = h2.next
        else:
            return list3

        # always use a temp pointer to iterate through a linked list, not the list variable itself
        curr = list3
        while(h1 != None or h2 != None):
            if(h1 != None and h2 != None and h1.val < h2.val):
                curr.next = ListNode(h1.val, next=None)
                h1 = h1.next
            elif(h1 != None and h2 != None and h1.val >= h2.val):
                curr.next = ListNode(h2.val, next=None)
                h2 = h2.next
            elif(h1 != None):
                curr.next = ListNode(h1.val, next=None)
                h1 = h1.next
            elif(h2 != None):
                curr.next = ListNode(h2.val, next=None)
                h2 = h2.next
            
            curr = curr.next
        
        return list3
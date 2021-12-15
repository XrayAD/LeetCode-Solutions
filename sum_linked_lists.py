# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        current = None
        while(l1 != None or l2 != None or carry==1):
            val = 0 + carry
            if (l1!= None):
                val += l1.val
            if(l2!= None):
                val+=l2.val
            if (val > 9):
                carry = 1
                val = val - 10
            else:
                carry = 0
            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next
            if (current is None):
                current = ListNode(val)
                number = current
            else:
                current.next = ListNode(val)
                current = current.next
        return number

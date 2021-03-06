# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        saver = ListNode(0)  #allows simplfication (no if statement on null head)
        saver.next = head
        prev = saver
        while(head):
            if head.val==val:
                prev.next=head.next
            else:
                prev=prev.next
            head=head.next
        return saver.next

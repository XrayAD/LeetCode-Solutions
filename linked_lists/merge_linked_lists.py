# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)  #having dummy starting node allows alot of simplification
        saver = head
        while (list1 and list2):
            if list1.val <= list2.val:
                saver.next = list1
                saver = list1
                list1=list1.next
            else:
                saver.next = list2
                saver = list2
                list2=list2.next
        if list1:                         #if one of lists is nonempty simply append at end
            saver.next = list1
        elif list2:
            saver.next = list2
        return head.next

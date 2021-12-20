class Solution:          #finds index recursively, shfits indices greater than n
    def removeNthFromEnd(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:       #my solution.
        total = 0
        saver = head
        while (saver):
            total += 1
            saver = saver.next
        remove = total - n
        saver = head
        if (remove == 0):
            return head.next
        while (remove > 0):
            prev = saver
            saver = saver.next
            remove -= 1
        prev.next = saver.next
        return head


class Solution1:   #puts fast pointer n ahead f slow pointer, at end slow points to node n+1 from back
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

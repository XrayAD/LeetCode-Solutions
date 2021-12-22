# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def show(self):
        arr = []
        head = self
        int = 0
        while(head and int < 10):
            arr.append(head.val)
            head = head.next
            int+=1
        print(arr)

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = None
        prev = None
        while(head is not None):
            if (head.next):
                swap_head = self.helper(head)
                if (start is None):          #preserve start of list
                    start = swap_head
                if (prev is None):           #preserve previous link before next swap (need to update chain after swap)
                    prev = swap_head.next
                else:
                    prev.next = swap_head
                    prev = swap_head.next
                head = swap_head.next.next
            else:
                if not prev:                #case with only one node
                    return head
                return start
        return start
    def helper(self, head: Optional[ListNode]) -> Optional[ListNode]:
        second = head.next              #next item in pair
        head.next = second.next         #fix head next
        second.next = head              #swap head and second
        return second                   #return first in list


def swapPairs(self, head):     # fast solution found online (pre.next evaluated before pre.next.next so so error thrown)
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next           # we creating dummy head node and can then return true node after this one

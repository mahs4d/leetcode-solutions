# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_next = head.next if head and head.next else None

        prev = None
        adj1 = head
        adj2 = head.next if head else None
        while adj1 and adj2:
            # swap
            adj1.next = adj2.next
            adj2.next = adj1
            if prev:
                prev.next = adj2
            
            prev = adj1
            adj1 = adj1.next
            adj2 = adj1.next if adj1 else None
            
        return head_next if head_next else head

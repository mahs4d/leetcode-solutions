class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        prev_del_node = None
        del_node = None
        cur_node, cur_i = head, 0
        while True:
            if del_node:
                prev_del_node = del_node
                del_node = del_node.next
            elif cur_i == n:
                del_node = head
            
            if cur_node is None:
                break
                
            cur_node = cur_node.next
            cur_i += 1


        if del_node is None:
            return head
        
        if del_node == head:
            return head.next

        prev_del_node.next = del_node.next
        return head

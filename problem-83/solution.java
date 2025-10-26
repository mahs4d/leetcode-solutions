/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode prev = head;
        ListNode current = head != null ? head.next : null;
        while (current != null) {
            if (current.val == prev.val) {
                // remove current node
                prev.next = current.next;
                current = current.next;
            } else {
                prev = current;
                current = current.next;
            }
        }

        return head;
    }
}

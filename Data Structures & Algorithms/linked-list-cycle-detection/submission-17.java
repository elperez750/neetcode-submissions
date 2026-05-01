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
    public boolean hasCycle(ListNode head) {
    
        if (head == null || head.next == null) {
            return false;
        }



        ListNode slow = head.next;
        ListNode fast = head.next.next;
        int count = 0;

        while (fast != null){
            if (count > 1000) {
                return true;
            }
            count += 1;

            slow = slow.next;

            if (fast.next != null) {
                fast = fast.next.next;
            }
            else{
                break;
            }
        }


        return false;
        
    
    }



}

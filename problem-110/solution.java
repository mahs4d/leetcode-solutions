/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }

        if (!isBalanced(root.left)) {
            return false;
        }

        if (!isBalanced(root.right)) {
            return false;
        }

        int leftDepth = getDepth(root.left);
        int rightDepth = getDepth(root.right);
        if (Math.abs(leftDepth - rightDepth) > 1) {
            return false;
        }

        return true;
    }

    public int getDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        return 1 + Math.max(
            getDepth(root.left),
            getDepth(root.right)
        );
    }
}
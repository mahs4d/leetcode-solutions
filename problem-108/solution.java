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
    public TreeNode sortedArrayToBST(int[] nums) {
        return getBst(nums, 0, nums.length);
    }

    public TreeNode getBst(int[] nums, int leftIndex, int rightIndex) {
        if (leftIndex >= rightIndex)
            return null;
        
        int middleIndex = (leftIndex + rightIndex) / 2;
        int nodeValue = nums[middleIndex];
        TreeNode left = getBst(nums, leftIndex, middleIndex);
        TreeNode right = getBst(nums, middleIndex + 1, rightIndex);
        return new TreeNode(nodeValue, left, right);
    }
}

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

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        Stack<Pair<TreeNode, Boolean>> stack = new Stack<>();
        if (root != null) {
            stack.push(new Pair<>(root, false));
        }

        while (!stack.isEmpty()) {
            var pair = stack.pop();
            var currentNode = pair.getKey();
            var isExtended = pair.getValue();

            if (isExtended) {
                result.add(currentNode.val);
                continue;
            }

            if (currentNode.right != null) {
                stack.push(new Pair<>(currentNode.right, false));
            }

            stack.push(new Pair<>(currentNode, true));

            if (currentNode.left != null) {
                stack.push(new Pair<>(currentNode.left, false));
            }
        }

        return result;
    }
}
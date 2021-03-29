/**
 *  0ms, faster than 100% of java sols
 *  39.5MB, less than 26.86% of java sols
 */

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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> levelOrder = new ArrayList<List<Integer>>();
        currLevel(root, levelOrder, 0);
        return levelOrder;
    }
    
    private void currLevel(TreeNode root, List<List<Integer>> levelOrder, int l){
        if (root == null) 
            return;
        if (l >= levelOrder.size()) 
            levelOrder.add(new LinkedList<Integer>());
        
        levelOrder.get(l).add(root.val);
        currLevel(root.left, levelOrder, l+1);
        currLevel(root.right, levelOrder, l+1);
    }
}

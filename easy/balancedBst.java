/**
 *  0ms, faster than 100% of java sols
 *  38.8MB, less than 48.82% of java sols
 *
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

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode() {}

    TreeNode(int val) { this.val = val; }

    TreeNode(int val, TreeNode left, TreeNode right){
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums.length == 0)
            return null; //nothing
        
        TreeNode root = sortedArrayToBSTHelper(nums, 0, nums.length);
        return root;
    }
    
    private TreeNode sortedArrayToBSTHelper(int[] nums, int start, int end){
        if(nums.length == 0)
            return null;
        if (start >= end)
            return null;
        
        int mid = (start + end)/2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = sortedArrayToBSTHelper(nums, start, mid);
        root.right = sortedArrayToBSTHelper(nums, mid+1, end);
            
            
        return root;
    }
}

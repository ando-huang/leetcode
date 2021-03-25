/**
 *  4ms, faster than 92.83% of C sols
 *  8MB, less than 63.76% of C sols
 *
 */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int maxDepth(struct TreeNode* root){
    if(root == NULL)
        return 0;
    return max(maxDepth(root->left), maxDepth(root->right)) + 1;
}

int max(int a, int b){
    if(a > b)
        return a;
    return b;
}

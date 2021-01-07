/**
    12ms, faster than 85.79% of C++ sols
    12MB, less than 90.94% of C++ sols
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL){
            return head;
        }
        ListNode* curr = head;
        while (curr->next != NULL){
            //condition to remove is if next->val == curr->val
            if(curr->val == curr->next->val){
                curr->next = curr->next->next;
                continue;
            }
            curr = curr->next;
        }
        return head;
    }
};

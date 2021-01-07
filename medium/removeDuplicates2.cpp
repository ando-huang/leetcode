/**
    32ms, faster than 10.78% of C++ sols
    11.6mb, less than 30.93% of C++ sols
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
        ListNode **curr = &head;
        
        if(!head || !head->next)return head;
        
        while(*curr)
        {
            if((*curr)->next && (*curr)->next->val == (*curr)->val)
            {
                ListNode *temp = *curr;
                while(temp && (*curr)->val == temp->val)
                    temp = temp->next;
                
                *curr = temp;
            }
            else
                curr = &((*curr)->next);
        }
        return head;
    }
};

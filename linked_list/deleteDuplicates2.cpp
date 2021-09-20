// leetcode 82. deleteDuplicatesII

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
    ListNode* deleteDuplicates(ListNode* head) 
    {
        if (!head)
        {
            return nullptr;
        }
        if (head->next && head->val == head->next->val)
        {
            while(head->next && head->val == head->next->val)
            {
                head = head->next;
            }
            return deleteDuplicates(head->next);
        }
        else
        {
            head->next = deleteDuplicates(head->next);
        }
        return head;
    }
};



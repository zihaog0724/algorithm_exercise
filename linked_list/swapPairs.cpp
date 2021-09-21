// leetcode 24. swapPairs

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
    ListNode* swapPairs(ListNode* head) 
    {
        if(!head)
        {
            return nullptr;
        }
        
        if(!head->next)
        {
            return head;
        }
        
        ListNode* node = head;
        for (int i = 0; i < 2; i++)
        {
            if(node)
            {
                node = node->next;
            }
        }
        ListNode* newHead = swap(head);
        head->next = swapPairs(node);
        return newHead;
    }

    ListNode* swap(ListNode* head)
    {
        ListNode* nex = head->next;
        head->next = nullptr;
        nex->next = head;
        return nex;
    }
};

// leetcode 21. mergeTwoLists

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) 
    {
        if (!l1 && !l2)
        {
            return nullptr;
        }
        if(!l1 && l2)
        {
            return l2;
        }
        if(l1 && !l2)
        {
            return l1;
        }

        ListNode* l = new ListNode(0);
        ListNode* head = l;
        while(l1 && l2)
        {
            if (l1->val <= l2->val)
            {
                l->next = new ListNode(l1->val);
                l1 = l1->next;
                l = l->next;
            }
            else
            {
                l->next = new ListNode(l2->val);
                l2 = l2->next;
                l = l->next;
            }
        }

        while(l1)
        {
            l->next = new ListNode(l1->val);
            l1 = l1->next;
            l = l->next;
        }

        while(l2)
        {
            l->next = new ListNode(l2->val);
            l2 = l2->next;
            l = l->next;
        }
        return head->next;
    }
};

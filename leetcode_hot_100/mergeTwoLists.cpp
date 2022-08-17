// hot100-lc 21. mergeTwoLists

#include "stdio.h"

struct ListNode{
    int val;
    ListNode* next;
    ListNode()
    {
        val = 0;
        next = nullptr;
    }
    ListNode(int x)
    {
        val = x;
        next = nullptr;
    }
    ListNode(int x, ListNode* Next)
    {
        val = x;
        next = Next;
    }
};


class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1 && !l2)
        {
            return nullptr;
        }
        if (!l1)
        {
            return l2;
        }
        if (!l2)
        {
            return l1;
        }

        ListNode node;
        ListNode* head = &node;
        while (l1 && l2)
        {
            if (l1->val <= l2->val)
            {
                head->next = l1;
                head = head->next;
                l1 = l1->next;
            }
            else
            {
                head->next = l2;
                head = head->next;
                l2 = l2->next;
            }
        }

        while (l1)
        {
            head->next = l1;
            head = head->next;
            l1 = l1->next;
        }

        while (l2)
        {
            head->next = l2;
            head = head->next;
            l2 = l2->next;
        }
        return node.next;
    }
};

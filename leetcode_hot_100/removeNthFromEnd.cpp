// hot100-lc 19. 

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head == nullptr)
        {
            return head;
        }

        ListNode* slow = head;
        ListNode* fast = head;

        for (int i = 0; i < n; i++)
        {
            fast = fast->next;
        }

        if (fast == nullptr)
        {
            return head->next;
        }

        while(fast->next)
        {
            slow = slow->next;
            fast = fast->next;
        }

        slow->next = slow->next->next;
        return head;
    }
};


int main()
{
    Solution solution;
    ListNode node1(2);
    ListNode node2(3);
    ListNode node3(1);
    ListNode node4(5);
    ListNode node5(4);
    ListNode node6(6);
    node1.next = &node2;
    node2.next = &node3;
    node3.next = &node4;
    node4.next = &node5;
    node5.next = &node6;
    ListNode* head = &node1;
    ListNode* ret = solution.removeNthFromEnd(head, 6);
    while(ret)
    {
        printf("%d ", ret->val);
        ret = ret->next;
    }
    return 0;
}


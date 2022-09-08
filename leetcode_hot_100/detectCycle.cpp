// hot100-lc 142. 环形链表-2

#include <cstdio>
#include <vector>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head)
    {
        if(!head or !head->next)
        {
            return nullptr;
        }

        ListNode* fast = head;
        ListNode* slow = head;
        while(fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast)
            {
                break;
            }
        }

        if(!fast or !fast->next)
        {
            return nullptr;
        }

        slow = head;
        while(slow != fast)
        {
            slow = slow->next;
            fast = fast->next;
        }
        return slow;
    }
};

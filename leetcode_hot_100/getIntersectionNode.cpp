// hot100-lc 160. 相交链表

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        ListNode* p1 = headA;
        ListNode* p2 = headB;

        while(p1 != p2)
        {
            p1 = p1->next;
            p2 = p2->next;
            if(!p1 && !p2)
            {
                return nullptr;
            }
            if(!p1)
            {
                p1 = headB;
            }
            if(!p2)
            {
                p2 = headA;
            }

        }
        return p1;
    }
};


// 剑指offer 52. getIntersectionNode

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) 
    {
        ListNode* nodeA = headA;
        ListNode* nodeB = headB;

        while(nodeA != nodeB)
        {
            if(nodeA)
            {
                nodeA = nodeA->next;
            }
            else
            {
                nodeA = headB;
            }

            if(nodeB)
            {
                nodeB = nodeB->next;
            }
            else
            {
                nodeB = headA;
            }
        }
        return nodeA;    
    }
};

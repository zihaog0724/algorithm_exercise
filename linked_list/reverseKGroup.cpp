// leetcode 25. reverseKGroup

struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(nullptr) {
	}
};


class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k)
    {
        ListNode* node = head;

        for (int i = 0; i < k; i++)
        {
            if (!node)
            {
                return head;
            }
            node = node->next;
        }

        ListNode* newHead = reverse(head, node);
        head->next = reverseKGroup(node, k);
        return newHead;
    }

    ListNode* reverse(ListNode* head, ListNode* node)
    {
        ListNode* cur = head;
        ListNode* nex = nullptr;
        ListNode* pre = nullptr;
        while (cur != node)
        {
            nex = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nex;
        }
        return pre;
    }
};

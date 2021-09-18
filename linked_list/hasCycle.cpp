// leetcode 141. hasCycle

struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(nullptr) {
	}
};


class Solution {
public:
    bool hasCycle(ListNode *head)
    {
        if (!head or !head->next)
        {
            return false;
        }
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast && fast->next)
        {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow)
            {
                return true;
            }
        }
        return false;
    }
};

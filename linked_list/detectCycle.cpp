//leetcode 142. detectCycle

struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(nullptr) {
	}
};


class Solution {
public:
    ListNode *detectCycle(ListNode *head)
    {
        if (!head or !head->next)
        {
            return nullptr;
        }

        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast)
            {
                break;
            }
        }

        if (!fast or !fast->next)
        {
            return nullptr;
        }

        /*
        判断相遇地点时：
        设a为链表起始到环入口的路程；
        设x为环入口到相遇点的路程；
        设c为环长；
        设slow走过路程为s，则fast走过路程为2s；
        则有s = a + x;
        2s = nc + s;
        推导有a + x = nc；
        a = nc - x = (n - 1)c + (c - x) = kc + (c - x)
        其中，c - x为从相遇点走回环入口的距离。
        则上式意味着，慢指针（step=1）从链表起始出发走过a到环入口的距离，
        等于快指针（step=1）从相遇点出发走过k圈，再走c-x的距离
        这个c-x的距离恰好使快指针也到达环入口
        */
        slow = head;
        while(slow != fast)
        {
            slow = slow->next;
            fast = fast->next;
        }
        return fast;
    }
};

#include <iostream>

struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(nullptr) {
	}
};

ListNode *reverseLinkedList(ListNode *pHead)
{
    if (pHead == nullptr)
    {
        return nullptr;
    }

    ListNode *pre, *cur, *nex;
    pre = nullptr;
    cur = pHead;
    nex = nullptr;

    while(cur)
    {
        nex = cur->next;
        cur->next = pre;
        pre = cur;
        cur = nex;
    }
    return pre;
}

int main()
{
    ListNode node1(3);
    ListNode node2(4);
    ListNode node3(5);
    node1.next = &node2;
    node2.next = &node3;
    ListNode *reversed = reverseLinkedList(&node1);
    std::cout << reversed->val << "; " <<  reversed->next->val << "; " << reversed->next->next->val << std::endl;
}

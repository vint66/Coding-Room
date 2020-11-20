# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    def traverse_ll(ll):
        if ll.next is None:
            return ll.val
        return traverse_ll(ll.next)

    print(traverse_ll(l1))
#             new_node = ListNode(head)

#         if traverse_llif traverse_ll
#         if l1.val <= l2.val:
#             new_node = ListNode(l1.val)
#             l1 = l1.next
#         else:
#             new_node = ListNode(l2.val)
#             l2 = l2.next
#         l3 = l3.next

#         while head1.next

ll1_3 = ListNode(4)
ll1_2 = ListNode(2, ll1_3)
ll1_1 = ListNode(1, ll1_2)

ll2_3 = ListNode(4)
ll2_2 = ListNode(3, ll2_3)
ll2_1 = ListNode(1, ll2_2)

mergeTwoLists(ll1_1, ll2_1)

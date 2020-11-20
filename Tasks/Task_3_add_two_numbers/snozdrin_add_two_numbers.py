# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def get_number_from_ll(ll):

            lst = str()

            if not ll.next:
                return ll.val

            lst += str(get_number_from_ll(ll.next)) + str(ll.val)

            return int(lst)

        def get_ll_from_number(num):
            str_num = str(num)
            head_node = ListNode(str_num[0])

            for i in str_num[1:]:
                new_node = ListNode(i)
                new_node.next = head_node
                head_node = new_node

            return head_node

        result = get_number_from_ll(l1) + get_number_from_ll(l2)
        return get_ll_from_number(result)


if __name__ == "__main__":
    pass

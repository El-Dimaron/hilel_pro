# Link:
# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_1 = self.node_to_num(l1)
        number_2 = self.node_to_num(l2)
        if number_1 == 0 and number_2 == 0:
            return l1
        result = number_1 + number_2
        print(result)
        return self.num_to_node(result)

    @staticmethod
    def node_to_num(node: ListNode) -> int:
        str_number = ""
        while True:
            if node is not None:
                str_number += str(node.val)
                node = node.next
            else:
                return int(str_number[::-1])

    def num_to_node(self, num: int, node=ListNode()) -> ListNode:
        if num:
            remainder = num % 10
            number = num // 10
            return ListNode(remainder, self.num_to_node(number, ListNode()))
        else:
            return None

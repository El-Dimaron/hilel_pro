# Link:
# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, node1: ListNode, node2: ListNode) -> ListNode:
        node = ListNode()
        current_node = node
        total = result_node = 0

        while node1 or node2 or result_node:
            total = result_node

            if node1:
                total += node1.val
                node1 = node1.next

            if node2:
                total += node2.val
                node2 = node2.next

            number = total % 10
            result_node = total // 10
            node.next = ListNode(number)
            node = node.next

        return current_node.next

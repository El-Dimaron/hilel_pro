# Link:
# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_1 = self.node_to_list(list1)
        list_2 = self.node_to_list(list2)
        result_list = self.merge_lists(list_1, list_2)
        return self.list_to_node(result_list)

    @staticmethod
    def node_to_list(node: ListNode) -> list[int]:
        list_number = []
        while True:
            if node is not None:
                list_number.append(node.val)
                node = node.next
            else:
                return list_number

    @staticmethod
    def merge_lists(list1: list[int], list2: list[int]) -> list[int]:
        merged_list = []
        pointer_1 = pointer_2 = 0
        while pointer_1 <= len(list1) - 1 or pointer_2 <= len(list2) - 1:
            if pointer_1 == len(list1):
                merged_list.extend(list2[pointer_2:])
                return merged_list
            if pointer_2 == len(list2):
                merged_list.extend(list1[pointer_1:])
                return merged_list

            if list1[pointer_1] <= list2[pointer_2]:
                merged_list.append(list1[pointer_1])
                pointer_1 += 1
            elif list1[pointer_1] > list2[pointer_2]:
                merged_list.append(list2[pointer_2])
                pointer_2 += 1
        return merged_list

    def list_to_node(self, list_number: list[int], node=ListNode()) -> ListNode:
        if list_number:
            return ListNode(list_number.pop(0), self.list_to_node(list_number, ListNode()))
        else:
            return None

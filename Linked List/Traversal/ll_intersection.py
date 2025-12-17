# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        ptr_A, ptr_B = headA, headB

        while ptr_A != ptr_B:
            ptr_A = ptr_A.next if ptr_A else headB
            ptr_B = ptr_B.next if ptr_B else headA
        return ptr_A

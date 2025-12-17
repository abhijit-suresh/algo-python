# https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr -> A
        curr = head
        # P -> None
        prev = None

        while curr:
            # T-> B
            temp = curr.next
            # A -> None
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        newHead = head
        if head.next:
            newHead = self.reverseList_recursive(head.next)
            head.next.next = head
        head.next = None
        return newHead

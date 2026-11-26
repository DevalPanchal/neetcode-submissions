# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = head

        k = 0
        curr = head

        # find length of list
        while curr:
            curr = curr.next
            k += 1

        # return head if n > k
        if n > k:
            return head

        # if head node needs to be deleted
        if k - n == 0:
            head = head.next
            return head

        # go to node before target node
        curr = head

        for i in range(1, k - n):
            curr = curr.next

        # delete node
        curr.next = curr.next.next

        return head




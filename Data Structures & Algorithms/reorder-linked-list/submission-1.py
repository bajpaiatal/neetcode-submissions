# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def merge(self, head1:Optional[ListNode], head2:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp1, temp2, temp = head1, head2, dummy
        while temp1 and temp2:
            temp.next = temp1
            temp1 = temp1.next
            temp = temp.next
            temp.next = temp2
            temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        if temp2:
            temp.next = temp2
        return dummy.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1, l2 = head, slow.next
        slow.next = None
        l2 = self.reverse(l2)
        head = self.merge(l1, l2)
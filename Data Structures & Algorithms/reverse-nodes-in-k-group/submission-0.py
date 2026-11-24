# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> None:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

    def findKNode(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = curr
        l = 1
        while l<k and temp:
            temp = temp.next
            l += 1
        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, curr = None, head
        while curr:
            kthNode = self.findKNode(curr, k)
            if not kthNode:
                prev.next = curr
                break
            nxt = kthNode.next
            kthNode.next = None
            self.reverse(curr)
            if not prev:
                head = kthNode
            else:
                prev.next = kthNode
            prev = curr
            curr = nxt
        return head
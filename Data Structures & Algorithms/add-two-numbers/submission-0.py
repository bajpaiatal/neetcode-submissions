# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode()
        temp1, temp2, temp = l1, l2, dummy
        summ = 0
        carry = 0
        while temp1 or temp2:
            if carry:
                summ += carry
            if temp1:
                summ += temp1.val
                temp1 = temp1.next
            if temp2:
                summ += temp2.val
                temp2 = temp2.next
            carry = summ//10
            summ = summ%10
            temp.next = ListNode(summ)
            temp = temp.next
            summ = 0
        if carry:
            temp.next = ListNode(carry)
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self, list1: ListNode, list2: ListNode) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp1, temp2, temp = list1, list2, dummy
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        if temp2:
            temp.next = temp2
        return dummy.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while True:
            if len(lists)==1:
                return lists[0]
            mergeLists = []
            for i in range(0, len(lists), 2):
                if i+1<len(lists):
                    mergeLists.append(self.merge2Lists(lists[i], lists[i+1]))
                else:
                    mergeLists.append(lists[i])
            lists = mergeLists
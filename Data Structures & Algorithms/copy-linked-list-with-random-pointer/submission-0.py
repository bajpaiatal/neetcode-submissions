"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def insertNewNodes(self, head: 'Optional[Node]') -> None:
        if not head:
            return None
        temp = head
        while temp:
            newNode = Node(temp.val, temp.next)
            temp.next = newNode
            temp = newNode.next

    def copyRandomNodes(self, head: 'Optional[Node]') -> None:
        temp = head
        while temp:
            newNode = temp.next
            if temp.random:
                newNode.random = temp.random.next
            temp = newNode.next
    
    def decouple(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        temp, temp2 = head, dummy
        while temp:
            temp2.next = temp.next
            temp.next = temp.next.next
            temp2 = temp2.next
            temp = temp.next
        return dummy.next

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        self.insertNewNodes(head)
        self.copyRandomNodes(head)
        return self.decouple(head)
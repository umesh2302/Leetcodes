# Definition for singly-linked list.
# https://leetcode.com/problems/add-two-numbers/editorial/?source=submission-ac
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_1 = []
        number_2 = []
        l1, number_1 = self.extract_number(l1,number_1 )
        l2, number_2 = self.extract_number(l2, number_2)
        total = self.add_number(number_1[::-1]) + self.add_number(number_2[::-1])
        reversed_total = self.reverse_number_list(total)
        return self.create_linked_list(reversed_total)

        return number
    def extract_number(self, l: Optional[ListNode], number: list) -> list:
        while l is not None:
            number.append(l.val)
            l = l.next
        return l, number
    
    def add_number(self, number: list) -> int:
        return int(''.join(map(str, number)))
    def reverse_number_list(self, number: int) -> int:
        return [int(x) for x in str(number)][::-1]
    def create_linked_list(self, number: list) -> Optional[ListNode]:
        head = ListNode()
        current = head
        for n in number:
            current.next = ListNode(n)
            current = current.next
        return head.next

# editortial solution
'''class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next'''


# Test
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
sol = Solution()
print(sol.addTwoNumbers(l1, l2)) # [7, 0, 8]



        


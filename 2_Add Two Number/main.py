from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Get values from the current nodes or 0 if the nodes are None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate the sum and carry
            _sum = x + y + carry
            carry = _sum // 10
            current.next = ListNode(_sum % 10)

            # Move to the next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            current = current.next

        return dummy_head.next

# Example usage:
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

solution_instance = Solution()
result = solution_instance.addTwoNumbers(l1, l2)

# Print the result
while result:
    print(result.val, end=" -> ")
    result = result.next

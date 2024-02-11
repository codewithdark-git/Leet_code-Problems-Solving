# Add Two Numbers

This Python code implements the Add Two Numbers problem solution using a linked list.

## Problem Statement
Given two non-empty linked lists representing two non-negative integers, where each node contains a single digit, add the two numbers and return the sum as a linked list.

## Approach
The code utilizes a dummy head node and a current node to build the result linked list. It iterates through both input linked lists simultaneously, adding corresponding digits along with any carry. The carry is propagated to the next iteration if needed. Once both lists are exhausted and there is no carry, the resulting linked list is returned.

## Complexity Analysis
- **Time Complexity:** The time complexity of this solution is O(max(m, n)), where m and n are the lengths of the input linked lists `l1` and `l2`, respectively. We iterate through both lists once.
- **Space Complexity:** The space complexity is O(max(m, n)) as we create a new linked list of the same length as the longer of the two input lists.

## Example
```python
# Example usage:
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

solution_instance = Solution()
result = solution_instance.addTwoNumbers(l1, l2)

# Print the result
while result:
    print(result.val, end=" -> ")
    result = result.next
# Output: 7 -> 0 -> 8
```
In this example, the input linked lists `l1` and `l2` represent the numbers 342 and 465, respectively. The sum of these two numbers is 807, which is represented by the linked list `7 -> 0 -> 8`.
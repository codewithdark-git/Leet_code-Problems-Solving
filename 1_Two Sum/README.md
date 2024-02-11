# Two Sum

This Python code implements the Two Sum problem solution using a dictionary to store the indices of elements.

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Approach
The code utilizes a dictionary `num_indices` to store the indices of elements as we iterate through the array `nums`. For each element `num` in `nums`, it calculates the complement needed to reach the `target` by subtracting `num` from `target`. If the complement is found in `num_indices`, it returns the indices of the two numbers that add up to the `target`. Otherwise, it adds the current element's index to `num_indices`. If no such pair is found, an empty list is returned.

## Complexity Analysis
- **Time Complexity:** The time complexity of this solution is O(n), where n is the number of elements in the input array `nums`. This is because we iterate through the array once.
- **Space Complexity:** The space complexity is also O(n) due to the usage of the `num_indices` dictionary to store the indices of elements.

## Example
```python
solution_instance = Solution()
nums = [2, 7, 11, 15]
target = 18
result = solution_instance.twoSum(nums, target)
print(result)  # Output: [1, 2]
```
In this example, the elements at indices 1 and 2 (7 and 11) add up to the target 18. Therefore, the function returns [1, 2] as the indices of these two numbers.
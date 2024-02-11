from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of elements
        num_indices = {}

        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_indices:
                # If found, return the indices of the two numbers
                return [num_indices[complement], i]

            num_indices[num] = i

        return []

solution_instance = Solution()
nums = [2, 7, 11, 15]
target = 18
result = solution_instance.twoSum(nums, target)
print(result)




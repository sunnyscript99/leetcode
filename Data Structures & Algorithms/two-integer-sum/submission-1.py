class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Quadratic Nested Loops
        # O(N^2) Time Complexity
        # O(1) Space Complexity
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Optimal Linear Hashmap Approach
        # O(N) Time Complexity
        # O(N) Space Complexity
        num_to_idx = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_to_idx:
                return [num_to_idx[diff], i]
            num_to_idx[num] = i

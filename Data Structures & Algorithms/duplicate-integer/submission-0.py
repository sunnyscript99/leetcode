class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute Force Quadratic Nested Loops
        # O(N^2) Time Complexity
        # O(1) Space Complexity
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Optimal Linear Hashset Approach
        # O(N) Time Complexity
        # O(N) Space Complexity
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

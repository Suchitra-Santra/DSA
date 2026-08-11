from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        i = 1

        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        nums_set = set(nums)

        while total in nums_set:
            total += 1

        return total


# Test
nums = [3, 4, 5, 1, 2]
sol = Solution()
print(sol.missingInteger(nums))
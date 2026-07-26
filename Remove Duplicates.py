class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

nums = [1, 1, 2, 2, 3]

solution = Solution()
k = solution.removeDuplicates(nums)

print("Number of unique elements:", k)
print("Array:", nums[:k])
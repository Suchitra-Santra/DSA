class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Update closest sum
                if abs(target - current_sum) < abs(target - closest):
                    closest = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return closest


# Input from user
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))

# Create object and call function
sol = Solution()
result = sol.threeSumClosest(nums, target)

print("Closest sum is:", result)
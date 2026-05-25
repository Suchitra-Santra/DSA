def three_sum(nums):
    nums.sort()  # Sort the array first
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for the second number
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # Skip duplicates for the third number
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1  # Need a bigger number
            else:
                right -= 1  # Need a smaller number

    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
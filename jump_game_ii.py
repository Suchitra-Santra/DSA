def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        # Reached the end of the current jump
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps


# Example
nums = [2, 3, 1, 1, 4]

print("Minimum jumps:", jump(nums))
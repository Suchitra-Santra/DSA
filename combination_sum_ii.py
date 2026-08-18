class Solution:
    def combinationSum2(self, candidates, target):
        result = []

        candidates.sort()

        def backtrack(start, target, path):
            if target == 0:
                result.append(path.copy())
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                if candidates[i] > target:
                    break

                path.append(candidates[i])

                # i + 1 because each number can be used only once
                backtrack(i + 1, target - candidates[i], path)

                path.pop()

        backtrack(0, target, [])
        return result


# Test in VS Code
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

solution = Solution()
print(solution.combinationSum2(candidates, target))

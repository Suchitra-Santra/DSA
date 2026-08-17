class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path.copy())
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                backtrack(
                    i,
                    target - candidates[i],
                    path
                )

                path.pop()

        backtrack(0, target, [])
        return result


# Test in VS Code
candidates = [2, 3, 6, 7]
target = 7

solution = Solution()
print(solution.combinationSum(candidates, target))
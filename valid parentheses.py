class Solution:
    def isValid(self, s):
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'

                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


s = input("Enter parentheses string: ")

sol = Solution()
print("Valid:", sol.isValid(s))
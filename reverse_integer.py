class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x != 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        rev *= sign

        # 32-bit signed integer check
        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev


# Run in VS Code
if __name__ == "__main__":
    x = int(input("Enter an integer: "))

    sol = Solution()
    result = sol.reverse(x)

    print("Reversed Integer:", result)
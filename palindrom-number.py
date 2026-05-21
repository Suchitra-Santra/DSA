class Solution:
    def isPalindrome(self, x):

        if x < 0:
            return False

        original = x
        reverse = 0

        while x != 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        return original == reverse


# Driver Code for VS Code
obj = Solution()

print(obj.isPalindrome(121))
print(obj.isPalindrome(-121))
print(obj.isPalindrome(10))
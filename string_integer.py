class Solution:
    def myAtoi(self, s):

        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        i = 0

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        num = 0

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num = num * sign

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN

        if num > INT_MAX:
            return INT_MAX

        return num


# Driver code for VS Code
obj = Solution()

print(obj.myAtoi("42"))
print(obj.myAtoi("   -42"))
print(obj.myAtoi("4193 with words"))
print(obj.myAtoi("words and 987"))
print(obj.myAtoi("-91283472332"))
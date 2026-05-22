class Solution:
    def intToRoman(self, num):

        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbol = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""

        i = 0

        while num > 0:

            while num >= val[i]:
                roman += symbol[i]
                num -= val[i]

            i += 1

        return roman


# Driver Code for VS Code
obj = Solution()

print(obj.intToRoman(3))
print(obj.intToRoman(58))
print(obj.intToRoman(1994))
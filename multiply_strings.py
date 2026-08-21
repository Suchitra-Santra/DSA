def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    result = [0] * (len(num1) + len(num2))

    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            digit1 = ord(num1[i]) - ord('0')
            digit2 = ord(num2[j]) - ord('0')

            product = digit1 * digit2

            pos1 = i + j
            pos2 = i + j + 1

            total = product + result[pos2]

            result[pos2] = total % 10
            result[pos1] += total // 10

    # Convert list of digits to string
    answer = ""

    for digit in result:
        if not (answer == "" and digit == 0):
            answer += str(digit)

    return answer


# Test
num1 = "123"
num2 = "456"

print("Result:", multiply(num1, num2))
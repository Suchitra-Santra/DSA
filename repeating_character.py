s = input("Enter string: ")

longest = 1
current = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        current += 1
    else:
        current = 1

    longest = max(longest, current)

print("Longest repeating substring length:", longest)
from collections import Counter

def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    word_count = Counter(words)
    result = []

    for i in range(len(s) - total_len + 1):
        seen = Counter()

        for j in range(0, total_len, word_len):
            word = s[i + j:i + j + word_len]

            if word not in word_count:
                break

            seen[word] += 1

            if seen[word] > word_count[word]:
                break
        else:
            result.append(i)

    return result


# Example
s = "barfoothefoobarman"
words = ["foo", "bar"]

print(findSubstring(s, words))
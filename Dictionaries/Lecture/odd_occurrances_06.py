words = input().split()
words_lower = []
for word in words:
    words_lower.append(word.lower())

word_count = {}

for word in words_lower:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    if count % 2 != 0:
        print(word, end=" ")

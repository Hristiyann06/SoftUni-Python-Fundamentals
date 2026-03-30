dictionary = {}

n = int(input())

for _ in range(n):
    word = input()
    synonym = input()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)

for word, synonyms in dictionary.items():
    print(f"{word} - {', '.join(synonyms)}")

wordsSet = set()
for _ in range(int(input())):
    wordsSet.add(input())
words = list(wordsSet)
words.sort()
words.sort(key=lambda x:len(x))
for word in words:
    print(word)
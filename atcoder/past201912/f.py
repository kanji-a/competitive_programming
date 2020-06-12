import re

S = input()

words = []

while True:
    m = re.search(r'[A-Z].*?[A-Z]', S)
    words.append(S[0:m.end()])
    if m.end() == len(S):
        break
    S = S[m.end():]

print(''.join(sorted(words, key=str.lower)))

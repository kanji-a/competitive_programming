import re

N = input()
A = list(map(int, input().split()))

B = list(map(bin, A))
print(min(map(lambda x: len(re.search('0*$', x).group()), B)))
import sys
input = lambda: sys.stdin.readline().rstrip() 
import collections
from operator import itemgetter

def resolve():
    N = int(input())
    S = [input() for _ in range(N)]

    counter = collections.Counter(S)

    max_freq = max(counter.values())
    most_freq = [k for k, v in counter.items() if v==max_freq]
    for i in sorted(most_freq):
        print(i)

if __name__ == '__main__':
    resolve()

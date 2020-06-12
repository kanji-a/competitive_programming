import sys
input = lambda: sys.stdin.readline().rstrip() 
import math
from functools import reduce

def resolve():
    K = int(input())

    ans = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            tmp = math.gcd(a, b)
            for c in range(1, K+1):
                ans += math.gcd(tmp, c)

    print(ans)

if __name__ == '__main__':
    resolve()

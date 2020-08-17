import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, K = LI()
    s = [I() for _ in range(N)]

    if 0 in s:
        print(N)
    else:
        ans = 0
        mul = 1
        r = 0
        for l in range(N):
            while r < N and mul * s[r] <= K:
                mul *= s[r]
                r += 1

            ans = max(r - l, ans)

            if r == l:
                r += 1
            else:
                mul //= s[l]

        print(ans)

if __name__ == '__main__':
    resolve()

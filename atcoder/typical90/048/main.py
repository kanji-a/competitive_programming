#!/usr/bin/env python3
import bisect, collections, copy, functools, heapq, itertools, math, operator, string, sys, typing
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9 + 7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, K = LI()
    AB = [LI() for _ in range(N)]

    hq = []
    for i, e in enumerate(AB):
        A, B = e
        heapq.heappush(hq, (-B, i, True))
    # print(hq)

    ans = 0
    for _ in range(K):
        s, i, is_part = heapq.heappop(hq)
        ans -= s
        if is_part:
            heapq.heappush(hq, (AB[i][1] - AB[i][0], i, False))
        # print(s, i, hq)

    print(ans)

if __name__ == '__main__':
    resolve()

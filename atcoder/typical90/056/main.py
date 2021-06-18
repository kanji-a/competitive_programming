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
    N, S = LI()
    AB = [LI() for _ in range(N)]

    # dp[i]: i円になるように購入できるか
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        A, B = AB[i]
        for j in range(S, 0, -1):
            if 0 <= j - A and dp[i][j-A]:
                dp[i+1][j] = True
            if 0 <= j - B and dp[i][j-B]:
                dp[i+1][j] = True
    # for i in dp:
    #     print(i)

    if dp[-1][-1]:
        ans_r = []
        s = S
        for i in range(N - 1, -1, -1):
            A, B = AB[i]
            if 0 <= s - A and dp[i][s-A]:
                ans_r.append('A')
                s -= A
            elif 0 <= s - B and dp[i][s-B]:
                ans_r.append('B')
                s -= B
        print(''.join(ans_r[::-1]))
    else:
        print('Impossible')

if __name__ == '__main__':
    resolve()

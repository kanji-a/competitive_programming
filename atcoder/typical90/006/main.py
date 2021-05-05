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
    S = SS()

    # first[i][j]: 文字iがj番目以降で初登場するインデックス
    first = [[-1] * (N + 1) for _ in range(26)]
    for i in range(26):
        for j in range(N - 1, -1, -1):
            if S[j] == chr(ord('a') + i):
                first[i][j] = j
            else:
                first[i][j] = first[i][j + 1]
    # for i in first:
    #     print(i)

    ans = []
    idx = 0
    for i in range(K):
        # このような処理を前処理によってスキップ
        # d = [-1] * 26
        # for j in range(idx, N - K + 1 + i):
        #     n = ord(S[j]) - ord('a')
        #     if d[n] == -1:
        #         d[n] = j
        # print(d)
        for j in range(26):
            if 0 <= first[j][idx] < N - K + 1 + i:
                ans.append(chr(ord('a') + j))
                idx = first[j][idx] + 1
                break

    print(''.join(ans))

if __name__ == '__main__':
    resolve()

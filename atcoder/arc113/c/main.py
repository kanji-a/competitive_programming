#!/usr/bin/env python3
import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    S = SS()
    len_S = len(S)

    ans = 0
    # 以下を見る
    # 連続する同じ2文字のインデックス
    # すでに出てきた文字 変更できない文字
    cnt = collections.Counter()
    for i in range(len_S - 1, 0, -1):
        cnt[S[i]] += 1
        if S[i] == S[i-1]:
            ans += len_S - i - cnt[S[i]]
            cnt = collections.Counter()
            cnt[S[i]] += len_S - i

    print(ans)

if __name__ == '__main__':
    resolve()

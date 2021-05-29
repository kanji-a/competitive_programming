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
    N = I()
    ac = []
    cnt = collections.Counter()
    for _ in range(2 * N):
        a, c = LSS()
        a = int(a)
        ac.append((a, c))
        cnt[c] += 1

    # 基本的に同じ色同士を組ませる
    # 違う色同士の組は各種高々1つずつ なぜなら2つあったらバラして同色同士を組ませられるから
    # Bが偶数個の場合、条件よりRとGは奇数個 このとき違う色の組はRGかRB, GBの2通り
    if cnt['R'] % 2 == 0 and cnt['G'] % 2 == 0 and cnt['B'] % 2 == 0:
        print(0)
        return

    ac.sort(key=lambda x: x[0])
    # print(ac)
    diff = {'BR': INF, 'GR': INF, 'BG': INF}
    for i in range(2 * N - 1):
        if ac[i][1] != ac[i+1][1]:
            pair = ''.join(sorted([ac[i][1], ac[i+1][1]]))
            diff[pair] = min(ac[i+1][0] - ac[i][0], diff[pair])
    # print(diff)

    if cnt['R'] % 2 == 0:
        print(min(diff['BG'], diff['BR'] + diff['GR']))
    if cnt['G'] % 2 == 0:
        print(min(diff['BR'], diff['GR'] + diff['BG']))
    if cnt['B'] % 2 == 0:
        print(min(diff['GR'], diff['BR'] + diff['BG']))

if __name__ == '__main__':
    resolve()

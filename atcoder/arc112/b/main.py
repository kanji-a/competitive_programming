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
    B, C = LI()

    # -1倍せずデクリメントする場合
    # -1倍した後デクリメントする場合
    # デクリメントした後-1倍する場合
    # -1倍した後デクリメントした後-1倍する場合
    # 作れる範囲かぶる場合注意
    if B == 0:
        ans = C // 2 + (C - 1) // 2 + 1
    elif B > 0:
        if -B + (C - 1) // 2 < B - C // 2:
            ans = ((C - 1) // 2 + (C - 1) // 2 + 1) + (C // 2 + max(C - 2, 0) // 2 + 1)
        else:
            ans = (B + max(C - 2, 0) // 2) - (-B - (C - 1) // 2) + 1
    else:
        if B + (C - 1) // 2 < -B - max(C - 2, 0) // 2:
            ans = ((C - 1) // 2 + (C - 1) // 2 + 1) + (C // 2 + max(C - 2, 0) // 2 + 1)
        else:
            ans = (-B + (C - 1) // 2) - (B - C // 2) + 1
    print(ans)

if __name__ == '__main__':
    resolve()

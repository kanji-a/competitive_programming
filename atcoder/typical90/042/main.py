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
    K = I()

    # 桁の和が9の倍数かつKであるもの
    if K % 9 != 0:
        print(0)
        return

    # dp[i]: 桁和がiである数の場合の数
    dp = [0] * (K + 1)
    dp[0] = 1

    for i in range(1, K + 1):
        tmp = 0
        for j in range(1, 10):
            # 0桁目がjのとき、1桁目以降の数を対象とする小問題に分解できる
            if 0 <= i - j:
                tmp += dp[i - j]
        tmp %= MOD
        dp[i] = tmp
    # print(dp)

    print(dp[-1])

if __name__ == '__main__':
    resolve()

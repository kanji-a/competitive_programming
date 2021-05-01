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
    S = [SS() for _ in range(4)]

    d = ((0, 0), (1, 0), (0, 1), (-1, 0), (0, -1))

    dp = [INF] * 2 ** 16
    dp[0] = 0

    for s_c in range(1, 2 ** 16):
        # どこを狙うのが最適か全探索
        for cy in range(4):
            for cx in range(4):
                # 的を外した数
                cnt = 0
                tmp = 0
                for dy, dx in d:
                    ny = cy + dy
                    nx = cx + dx
                    # 今の状態と次の状態が異なる場合の処理
                    if 0 <= ny < 4 and 0 <= nx < 4 and s_c >> (ny * 4 + nx) & 1:
                        s_n = s_c & ~(1 << (ny * 4 + nx))
                        tmp += (1 + dp[s_n]) / 5
                    # 今の状態と次の状態が同じ場合の処理
                    else:
                        cnt += 1
                        tmp += 0.2
                if cnt != 5:
                    dp[s_c] = min(tmp * 5 / (5 - cnt), dp[s_c])

    s_d = {'.': '0', '#': '1'}
    ans = dp[int(''.join(''.join(s_d[j] for j in i) for i in S), 2)]
    print(ans)

if __name__ == '__main__':
    resolve()

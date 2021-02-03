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
    H, W, K = LI()
    S = [SS() for _ in range(H)]

    ans = INF
    # 行での切り方をbit全探索
    for i in range(2 ** (H - 1)):
        # 行をグループ分け
        g = [0] * H
        for j in range(H - 1):
            g[j+1] = g[j] + (i >> j & 1)
        g_num = g[-1] + 1
        # print(g)

        # グループごとに行をマージ 1列でK超えたらアウト
        is_over = False
        S_ = [[0] * W for _ in range(g_num)]
        for i in range(H):
            for j in range(W):
                S_[g[i]][j] += int(S[i][j])
                if S_[g[i]][j] > K:
                    is_over = True
        if is_over:
            continue
        # for i in S_:
        #     print(i)

        # 行方向に貪欲法で切り分ける
        white_num = [0] * g_num
        vertical_slash = 0
        for j in range(W):
            # K個より多くなる行グループの有無をチェック
            white_num = [white_num[k] + S_[k][j] for k in range(g_num)]
            if max(white_num) > K:
                # オーバーするならリセット
                white_num = [S_[k][j] for k in range(g_num)]
                vertical_slash += 1
        #     print(white_num)
        # print(vertical_slash)
        ans = min(g[-1] + vertical_slash, ans)

    print(ans)

if __name__ == '__main__':
    resolve()


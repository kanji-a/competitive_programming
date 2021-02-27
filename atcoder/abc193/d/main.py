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
    K = I()
    S = SS()
    T = SS()

    # 裏のカードで点数はi*9*10**cnt[i]だけ増える
    cnt_S = collections.Counter(int(i) for i in S[:4])
    cnt_T = collections.Counter(int(i) for i in T[:4])
    cnt_ST = cnt_S + cnt_T
    score_S = sum(i * 10 ** cnt_S[i] for i in range(1, 10))
    score_T = sum(i * 10 ** cnt_T[i] for i in range(1, 10))
    # print(cnt_S, cnt_T, cnt_ST, score_S, score_T)

    # 裏のカードの組み合わせは81通り
    # その中で高橋くんが勝つ組み合わせの確率はいくらか
    ans = 0
    for i in range(1, 10):
        if cnt_ST[i] == K:
            continue
        cnt_ST[i] += 1
        for j in range(1, 10):
            if cnt_ST[j] == K:
                continue
            if score_S + i * 9 * 10 ** cnt_S[i] > score_T + j * 9 * 10 ** cnt_T[j]:
                # print(i, j)
                if i == j:
                    rest_ij = K - cnt_S[i] - cnt_T[i]
                    ans += rest_ij * (rest_ij - 1)
                else:
                    rest_i = K - cnt_S[i] - cnt_T[i]
                    rest_j = K - cnt_S[j] - cnt_T[j]
                    ans += rest_i * rest_j
        cnt_ST = cnt_S + cnt_T
    
    print(ans / ((9 * K - 8) * (9 * K - 9)))

if __name__ == '__main__':
    resolve()

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
    a = LI()

    cnt = collections.Counter(a)

    # OKな必要十分条件: ベスト1が1人、ベスト2^xが2^(x-1)人であること。
    # aは2の累乗という条件があるので、ベスト1が1人、ベストxがx//2人であること、でよい。
    cnt_ok = {2 ** (i + 1): 2 ** i for i in range(N)}
    cnt_ok[1] = 1
    print(cnt, cnt_ok)
    if cnt != cnt_ok:
        print(-1)
        sys.exit()

    # 順位の並びを決めてから、その順位になる人の番号を割り振る
    # 8人だとしたら、順位を1 8 4 8 2 8 4 8のような並び方にしたい
    rank = [0] * 2 ** N

    # 順位: 人の番号一覧 という辞書を作り、答えを作る
    dict_rank_num = {k: [i[0] for i in g] for k, g in itertools.groupby(sorted(enumerate(a), key=lambda x: x[1]), key=lambda x: x[1])}
    print(dict_rank_num)
    ans = [0] * 2 ** N
    for i in range(2 ** N):
        ans[i] = dict_rank_num[rank[i]].pop()
    print(*ans)

if __name__ == '__main__':
    resolve()

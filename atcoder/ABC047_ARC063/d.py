import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, T = LI()
    A = LI()

    # i < jでAj - Aiがmaxになるようなペア全てに対してAjを下げる
    # 左側累積minと右側累積maxを持てばよい
    acm_min_l = [INF] * (N + 1)
    for i in range(N):
        acm_min_l[i+1] = min(acm_min_l[i], A[i])
    # print(acm_min_l)
    acm_max_r = [0] * (N + 1)
    for i in range(N-1, -1, -1):
        acm_max_r[i] = max(acm_max_r[i+1], A[i])
    # print(acm_max_r)

    price_diff_max = max([acm_max_r[i] - acm_min_l[i+1] for i in range(N)])

    # 数に対してインデックス持つ
    A_idx = collections.defaultdict(int)
    for i in range(N):
        A_idx[A[i]] = i
    # print(A_idx) 

    # 値段幅が最大になるようなペアをカウント
    ans = len([i for i in range(N) if A_idx[A[i]+price_diff_max] > i])

    print(ans)

if __name__ == '__main__':
    resolve()

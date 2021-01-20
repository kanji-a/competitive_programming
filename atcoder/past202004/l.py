import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
import atcoder.segtree as segtree
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
    N, K, D = LI()
    A = LI()

    if N < D * (K - 1) + 1:
        print(-1)
        return

    st = segtree.SegTree(min, INF, N)
    for i in range(N):
        st.set(i, A[i])
    
    # 先頭から、選択可能範囲[l:r)の最小値を持つAを貪欲法で選んでいく
    ans = []
    l = 0
    r = N - D * (K - 1)
    for i in range(K):
        # i文字目の選択
        m = st.prod(l, r)
        ans.append(m)
        # 区間の更新
        l = A.index(m, l, r)
        l += D
        r += D

    print(*ans)

if __name__ == '__main__':
    resolve()

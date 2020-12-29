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
    N, Q = LI()
    A = LI()
    st = segtree.SegTree(max, -1, A)
    for _ in range(Q):
        query = LI()
        T = query[0]
        if T == 1:
            X, V = query[1:]
            st.set(X - 1, V)
        elif T == 2:
            L, R = query[1:]
            ans = st.prod(L - 1, R)
            print(ans)
        else:
            X, V = query[1:]
            idx = st.max_right(X - 1, lambda x: x < V)
            print(idx + 1)

if __name__ == '__main__':
    resolve()

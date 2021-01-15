import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
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
    N, W, C = LI()

    # [l, r)でpかかる、としてからCの区間を考えるのは難しい
    # [車の左端の座標)でpかかる、とするとよい
    imos = collections.defaultdict(int)
    for _ in range(N):
        l, r, p = LI()
        imos[max(l-C+1,0)] += p
        imos[r] -= p
    # 門の右端から重さ∞の石があるとみなす
    imos[max(W-C+1,0)] += INF

    acm = []
    pre = 0
    for k, v in sorted(imos.items()):
        pre += v
        acm.append((k, pre))

    ans = min([i[1] for i in acm])
    print(ans)

if __name__ == '__main__':
    resolve()

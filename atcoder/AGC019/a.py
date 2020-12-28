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
    Q, H, S, D = LI()
    N = I()

    # 小数が出ないように量を4倍するする
    N *= 4
    L = [(1, Q), (2, H), (4, S), (8, D)]
    L.sort(key=lambda x: 8 // x[0] * x[1])
    # print(L)

    # 一番コスパいい量から買っていく
    ans = 0
    for v, p in L:
        ans += N // v * p
        N %= v

    print(ans)

if __name__ == '__main__':
    resolve()

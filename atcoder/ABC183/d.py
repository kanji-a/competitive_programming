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
    N, W = LI()
    STP = [LI() for _ in range(N)]
    imos = [0] * (max(i[1] for i in STP) + 1)
    for i in range(N):
        S, T, P = STP[i]
        imos[S] += P
        imos[T] -= P

    imos_acm = [0] * (len(imos) + 1)
    for i in range(len(imos)):
        imos_acm[i+1] = imos[i] + imos_acm[i]

    # print(imos)
    # print(imos_acm)
    if max(imos_acm) <= W:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()

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
    N, M, Q = LI()
    G = collections.defaultdict(list)
    for _ in range(M):
        u, v = LI_()
        G[u].append(v)
        G[v].append(u)
    c = LI()

    for _ in range(Q):
        s = LI()
        if s[0] == 1:
            x = s[1] - 1
            print(c[x])
            for i in G[x]:
                c[i] = c[x]
        else:
            x, y = s[1:]
            x -= 1
            print(c[x])
            c[x] = y

if __name__ == '__main__':
    resolve()

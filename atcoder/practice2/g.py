import bisect, collections, copy, heapq, itertools, math, operator, string, sys, typing
import atcoder.scc as scc
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
    N, M = LI()
    g = scc.SCCGraph(N)
    for _ in range(M):
        a, b = LI()
        g.add_edge(a, b)
    
    ans = g.scc()

    print(len(ans))
    for i in ans:
        print(len(i), *i)

if __name__ == '__main__':
    resolve()

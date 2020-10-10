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
    H, W = LI()
    S = [SS() for _ in range(H)]

    ans = 0
    for i in S:
        l = [len(list(g)) for k, g in itertools.groupby(i) if k == '.']
        ans += sum([max(j - 1, 0) for j in l])
    for i in range(W):
        s = [S[j][i] for j in range(H)]
        l = [len(list(g)) for k, g in itertools.groupby(s) if k == '.']
        ans += sum([max(j - 1, 0) for j in l])

    print(ans)

if __name__ == '__main__':
    resolve()

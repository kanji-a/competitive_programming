import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N = I()
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = LI_()
        G[a].append(b)
        G[b].append(a)
    c = LI()
    c.sort()

    # 最大の数は使われない、2番目に大きい数は、最大の数の隣のときだけ使われる
    # 深くなるほど小さくなるように置けば良い
    # DFSで置いていく
    ans = [0] * N
    def dfs(cur):
        ans[cur] = c.pop()
        for nxt in G[cur]:
            if ans[nxt] == 0:
                dfs(nxt)

    dfs(0)

    print(sum(ans[1:]))
    print(*ans)

if __name__ == '__main__':
    resolve()

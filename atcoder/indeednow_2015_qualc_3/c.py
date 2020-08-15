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

    ans = []

    hq = [0]
    visited = [False] * N
    visited[0] = True
    while hq:
        c = heapq.heappop(hq)
        ans.append(c + 1)
        for i in G[c]:
            if not visited[i]:
                visited[i] = True
                heapq.heappush(hq, i)

    print(*ans)

if __name__ == '__main__':
    resolve()

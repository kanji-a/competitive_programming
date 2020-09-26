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
    n = I()
    m = I()
    G = collections.defaultdict(list)
    for _ in range(m):
        a, b = LI_()
        G[a].append(b)
        G[b].append(a)

    que = collections.deque([0])
    dist = [INF] * n
    dist[0] = 0
    while que:
        c = que.popleft()
        for n in G[c]:
            if dist[n] > dist[c] + 1:
                dist[n] = dist[c] + 1
                que.append(n)

    ans = len([i for i in dist if 1 <= i <= 2])
    print(ans)

if __name__ == '__main__':
    resolve()
